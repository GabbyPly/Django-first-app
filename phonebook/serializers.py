from asyncore import read
from rest_framework import serializers
from phonebook.models import Contact
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "contacts"]


class ContactSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Contact
        fields = ["id", "name", "linenos", "language", "style", "code", "owner", "highlighted"]
