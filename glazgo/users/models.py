from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    ROLES = [
        (1, "Рекрутер"),
        (2, "Рекрутер-администратор"),
        (3, "Заказчик"),
        (4, "Заказчик-администратор"),
    ]

    role = models.IntegerField("Права", choices=ROLES, default=1)
    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    phone = models.CharField("Телефон", max_length=15)
    bio = models.CharField(max_length=255, null=True, blank=True)
    cover_photo = models.ImageField(upload_to="covers/", null=True, blank=True)
