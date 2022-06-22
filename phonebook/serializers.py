from asyncore import read
from rest_framework import serializers
from phonebook.models import Contact


class ContactSerializer(serializers.Serializer):
    # created = serializers.DateTimeField(required=False, auto_now_add=True)
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    number = serializers.CharField(max_length=255, allow_blank=True)  # , blank=True
    address = serializers.CharField(max_length=255, allow_blank=True)  # , blank=True
    # code = serializers.CharField(style={"base_template": "index.html"})  # What's this

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.number = validated_data.get("number", instance.number)
        instance.created = validated_data.get("created", instance.created)
        instance.address = validated_data.get("address", instance.address)
        # instance.code = validated_data.get("code", instance.code)  # What's this

        instance.save()
        return instance
