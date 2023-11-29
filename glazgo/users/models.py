from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = [
        (0, "Администратор"),
        (1, "Рекрутер"),
        (2, "Рекрутер-администратор"),
        (3, "Заказчик"),
        (4, "Заказчик-администратор"),
    ]
    # Необходимые поля
    referral_token = models.CharField(max_length=255)
    role = models.IntegerField("Права", choices=ROLES, default=1)
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=150)
    phone = models.CharField("Телефон", max_length=15)
    email = models.EmailField("Электронная Почта")

    # Опционально
    birthday = models.DateField("Дата рождения", null=True)
    bio = models.CharField("Биография", max_length=255, null=True)
    cover_photo = models.ImageField(upload_to="covers/", null=True)
    company_name = models.CharField("Название организации", max_length=30, null=True)
    description = models.TextField("Описание организации", null=True)
    legal_address = models.CharField("Юридический адрес", max_length=250, null=True)
    mailing_address = models.CharField("Почтовый адрес", max_length=250, null=True)
    inn = models.CharField("ИНН", max_length=10, null=True)
    checking_account = models.CharField("Расчетный счет", max_length=20, null=True)
    date_joined = models.DateTimeField("Дата регистрации", auto_now_add=True)