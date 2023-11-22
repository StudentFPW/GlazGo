from django.db import transaction

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import *


class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.role = self.data.get("role")
        user.first_name = self.data.get("first_name")
        user.last_name = self.data.get("last_name")
        user.email = self.data.get("email")
        user.phone = self.data.get("phone")
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "role",
            "first_name",
            "last_name",
            "email",
            "phone",
        )


class ULUSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
