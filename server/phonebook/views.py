from multiprocessing import AuthenticationError
from phonebook.models import Contact
from phonebook.serializers import ContactSerializer, UserSerializer
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


class RegisterViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        print("request", request)
        username = request.data["username"]
        password = request.data["password"]

        # user = User.objects.get(email=email)
        user = User.objects.filter(username=username).first()
        print("user", user)

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationError("Incorrect password")

        # return JsonResponse(user)
        return Response({"success": True})


class ContactViewSet(viewsets.ModelViewSet):
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
