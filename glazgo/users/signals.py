from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Users


@receiver(post_save, sender=Users)
def RoleRecognizer(instance, created, **kwargs):
    if not created:
        return

    if instance.role == 1:
        pass
    if instance.role == 2:
        pass
    if instance.role == 3:
        pass
    if instance.role == 4:
        pass
