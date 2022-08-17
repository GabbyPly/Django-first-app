from multiprocessing import AuthenticationError

from django.shortcuts import redirect
from phonebook.models import Contact, Post
from phonebook.serializers import ContactSerializer, UserSerializer, PostSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from phonebook.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.AllowAny,]


class LoginView(APIView):
    def post(self, request):
        print("request", request)
        username = request.data["username"]
        password = request.data["password"]
        return_to = request.GET.get("return_to", None)

        # user = User.objects.get(email=email)
        user = User.objects.filter(username=username).first()
        print("user", user)

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationError("Incorrect password")

        #  Should have used the 'authenticate' method from 'django.contrib.auth' ?
        login(request, user)
        data = request.data
        if return_to is not None:
            print("return to is", return_to)
            response = redirect(return_to)  # redirecting to home page
            return response

        return Response({"success": True})


class ContactViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    login_url = "/login/"
    redirect_field_name = "return_to"
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Optional url_path argument
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        contact = self.get_object()
        return Response(contact.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)  # <-- And here

    # Should this be here or on the serializer itself ? What's the difference
    def perform_create(self, serializer):
        post_instance = serializer.save(author=self.request.user)
        return Response(post_instance)

    def list(self, request, *args, **kwargs):
        print("request", request)
        print("request.headers", request.headers)
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
