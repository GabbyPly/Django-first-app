from rest_framework.serializers import ModelSerializer
from base.models import Room  # Change to phonebook.contacts


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room  # Change to phonebook.contacts
        fields = "__all__"
