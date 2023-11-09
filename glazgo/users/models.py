from django.db import models
from django.contrib.auth.models import AbstractUser
from ats.models import Customer


class Users(AbstractUser):
    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    otch = models.CharField("Отчество", max_length=20, null=True)
    birthday = models.DateField("Дата рождения")
    email = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=15)
    tlg = models.CharField("Телеграм", max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"id: {self.pk}, name: {self.name}, surname: {self.surname}"
