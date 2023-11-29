import secrets

from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from referral_system.models import ReferralCode


@receiver(post_save, sender=User)
def RoleRecognizer(instance, **kwargs):
    if not instance.is_superuser:
        user = User.objects.get(id=instance.pk)
        if instance.role == 1:
            group = Group.objects.get(name="UR")
        elif instance.role == 2:
            group = Group.objects.get(name="URA")
        elif instance.role == 3:
            group = Group.objects.get(name="UC")
        elif instance.role == 4:
            group = Group.objects.get(name="UCA")
        user.groups.add(group)
        return user
    User.objects.filter(id=instance.pk).update(role=0)
    for i in range(100):
        create_reftoken(instance)


def create_reftoken(user):
    """
    Функция создает случайный токен и сохраняет его вместе с
    пользователем в модели ReferralCode.

    param user:
        Параметр user — это объект, представляющий пользователя,
        для которого создается реферальный токен
    """
    token = secrets.token_urlsafe(5)
    ReferralCode(token=token, user=user).save()
