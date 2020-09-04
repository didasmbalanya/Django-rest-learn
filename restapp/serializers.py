from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Task


class UserSerializier(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class TaskSerializers(serializers.ModelSerializer):
    """
    Transform python data to Json format for sending over HTTP
    """

    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Task
        fields = ('id', 'task_name', 'task_description', 'completed',
                  'date_created', 'image')
