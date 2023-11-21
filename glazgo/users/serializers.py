from rest_framework import serializers

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "role",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
        ]


class ULUSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
