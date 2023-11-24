from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import transaction

from rest_framework import serializers
from allauth.account.adapter import get_adapter

from .models import User


class CustomRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "role",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
        )

    def get_cleaned_data(self):
        return {
            "username": self.validated_data.get("username", ""),
            "role": self.validated_data.get("role", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "email": self.validated_data.get("email", ""),
            "phone": self.validated_data.get("phone", ""),
            "password": self.validated_data.get("password", ""),
        }

    @transaction.atomic
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self, commit=False)
        if "password" in self.cleaned_data:
            try:
                adapter.clean_password(self.cleaned_data["password"], user=user)
            except DjangoValidationError as exc:
                raise serializers.ValidationError(
                    detail=serializers.as_serializer_error(exc)
                )
        user.save()
        return user


class UserDetailsSerializer(serializers.ModelSerializer):
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


# Этот метод работает пожалуйста не удалять ! ↓

# from dj_rest_auth.registration.serializers import RegisterSerializer
# from django.db import transaction

# class CustomRegisterSerializer(RegisterSerializer):
#     role = serializers.IntegerField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()

#     @transaction.atomic
#     def save(self, request):
#         user = super().save(request)
#         user.role = self.data.get("role")
#         user.first_name = self.data.get("first_name")
#         user.last_name = self.data.get("last_name")
#         user.email = self.data.get("email")
#         user.phone = self.data.get("phone")
#         user.save()
#         return user