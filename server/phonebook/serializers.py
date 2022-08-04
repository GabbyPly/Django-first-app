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


class UserSerializer(serializers.ModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(many=True, view_name="contact-detail", read_only=True)

    class Meta:
        model = User
        fields = ["url", "id", "username", "contacts", "password"]
        extra_kwargs = {"password": {"write_only": True}}  # note pw/password

    def create(self, validated_data):
        print("val data", validated_data)
        pw = validated_data.pop("password", None)
        # user_instance = User(**validated_data)
        user_instance = self.Meta.model(**validated_data)
        if pw is not None:
            user_instance.set_password(pw)
        user_instance.save()
        print("user_instance")
        print(user_instance)
        return user_instance
