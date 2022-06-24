from asyncore import read
from rest_framework import serializers
from phonebook.models import Contact
from django.contrib.auth.models import User


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(view_name="contact-highlight", format="html")

    class Meta:
        model = Contact
        fields = ["url", "id", "name", "linenos", "language", "style", "code", "owner", "highlight"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(many=True, view_name="contact-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "contacts"]
