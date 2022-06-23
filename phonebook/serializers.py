from asyncore import read
from rest_framework import serializers
from phonebook.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "linenos", "language", "style", "code", "owner", "highlighted"]
