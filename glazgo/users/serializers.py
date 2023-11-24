import secrets

from django.db import transaction

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User
from referral_system.models import ReferralRelationship, ReferralCode


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
        if not self.data.get("referral_token"):
            raise ValueError("Please use your token!")
        if not self.data.get("email"):
            raise ValueError("Users must have an email address!")
        if not self.data.get("username"):
            raise ValueError("Users must have an username!")

        username_r = self.data.get("username")
        email_r = self.data.get("email")
        referral_token_r = self.data.get("referral_token")
        role_r = self.data.get("role")
        first_name_r = self.data.get("first_name")
        last_name_r = self.data.get("last_name")
        phone_r = self.data.get("phone")

        # Этот блок кода проверяет, не равно ли значение переменной role_r 0. Если оно не равно 0, он
        # выполняет следующие действия:
        if not role_r == 0:
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

                # создает для пользователя 30 реферальных токенов.
                for i in range(30):
                    self.create_reftoken(user)
            else:
                raise ValueError("This token is used!")
            return user

        # Ненадежно в будущем нужно переконструировать !!!
        user.username = username_r
        user.email = email_r
        user.referral_token = referral_token_r
        user.role = role_r
        user.first_name = first_name_r
        user.last_name = last_name_r
        user.phone = phone_r
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        for i in range(100):
            self.create_reftoken(user)
        return user

    def create_reftoken(self, user):
        """
        Функция создает случайный токен и сохраняет его вместе с
        пользователем в модели ReferralCode.

        param user:
                Параметр user — это объект, представляющий пользователя,
                для которого создается реферальный токен
        """
        token = secrets.token_urlsafe(10)
        ReferralCode(token=token, user=user).save()


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


# Пожалуйста не удалять !!!
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
