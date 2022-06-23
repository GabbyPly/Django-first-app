from phonebook.models import Contact
from phonebook.serializers import ContactSerializer
from rest_framework import generics


class ConatctList(generics.ListCreateAPIView):
    """
    List all contacts, or create a new contact.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ConatctDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contact instance.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
