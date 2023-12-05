import secrets
import random

from django.db import transaction
from django.contrib.auth.models import Group

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from referral_system.models import ReferralRelationship, ReferralCode
from .models import User


def create_reftoken(user):
    """
    Функция создает случайный токен и сохраняет его вместе с
    пользователем в модели ReferralCode.

    param user:
        Параметр user — это объект, представляющий пользователя,
        для которого создается реферальный токен
    """
    token = secrets.token_urlsafe(random.randint(25, 30))
    ReferralCode(token=token, user=user).save()


class CustomRegisterSerializer(RegisterSerializer):
    """
    Класс CustomRegisterSerializer является подклассом RegisterSerializer,
    который добавляетдополнительные поля и настраиваемую логику сохранения
    для регистрации пользователя.
    """

    role = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    referral_token = serializers.CharField()

    @transaction.atomic
    def save(self, request):
        user = super().save(request)

        username_r = self.data.get("username")
        email_r = self.data.get("email")
        referral_token_r = self.data.get("referral_token")
        role_r = self.data.get("role")
        first_name_r = self.data.get("first_name")
        last_name_r = self.data.get("last_name")
        phone_r = self.data.get("phone")

        if not referral_token_r:
            raise ValueError("Please use your token!")
        if not email_r:
            raise ValueError("Users must have an email address!")
        if not username_r:
            raise ValueError("Users must have an username!")
        if not role_r:
            raise ValueError("Users must have an role!")
        if not first_name_r:
            raise ValueError("Users must have an first_name!")
        if not last_name_r:
            raise ValueError("Users must have an last_name!")
        if not phone_r:
            raise ValueError("Users must have an phone!")

        if role_r >= 1 and role_r <= 4:
            ref_code = ReferralCode.objects.filter(token=referral_token_r)
            if not ref_code:
                raise ValueError("Your token is not valid!")
            usages_token = ReferralRelationship.objects.filter(refer_token=ref_code[0])
            if not usages_token:
                user.username = username_r
                user.email = email_r
                user.referral_token = referral_token_r
                user.role = role_r
                user.first_name = first_name_r
                user.last_name = last_name_r
                user.phone = phone_r
                user.save()
                ReferralRelationship(
                    employer=ref_code[0].user,
                    employee=user,
                    refer_token=ref_code[0],
                ).save()

                if role_r == 1:
                    group = Group.objects.get(name="URA")
                if role_r == 2:
                    group = Group.objects.get(name="UCA")
                if role_r == 3:
                    group = Group.objects.get(name="UR")
                if role_r == 4:
                    group = Group.objects.get(name="UC")
                if role_r == 1 or role_r == 2:
                    for i in range(5):
                        create_reftoken(user)
                user.groups.add(group)
            else:
                raise ValueError("This token is used!")
            return user
        raise ValueError("Incorrect role!")


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "role",
            "referral_token",
            "email",
            "first_name",
            "last_name",
            "phone",
            "birthday",
            "bio",
            "cover_photo",
            "company_name",
            "description",
            "legal_address",
            "mailing_address",
            "inn",
            "checking_account",
            "date_joined",
        )


class ULUSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
