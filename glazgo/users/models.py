from django.db import models
from django.contrib.auth.models import AbstractUser

from ats.models import Customer


class Users(AbstractUser):
    # customer = models.ForeignKey(Customer, on_delete=models.PROTECT)  # FIXME NOT WORKING OR REGISTRATION

    name = models.CharField("Имя", max_length=20)
    surname = models.CharField("Фамилия", max_length=20)
    birthday = models.DateField("Дата рождения", null=True, blank=True)
    phone = models.CharField("Телефон", max_length=15)
    bio = models.CharField(max_length=255, null=True, blank=True)
    cover_photo = models.ImageField(upload_to="covers/", null=True, blank=True)
