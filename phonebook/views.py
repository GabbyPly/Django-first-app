from phonebook.models import Contact
from phonebook.serializers import ContactSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from phonebook.permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactList(generics.ListCreateAPIView):
    """
    List all contacts, or create a new contact.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        print("self.request", self.request)
        print("self.request.__dict__", self.request.__dict__)
        print("self.request.user", self.request.user)
        serializer.save(owner=self.request.user)


class ConatctDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contact instance.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
