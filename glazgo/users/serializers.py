from rest_framework import serializers

from .models import *


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["username"]
