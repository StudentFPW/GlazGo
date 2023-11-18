from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Users


@receiver(post_save, sender=Users)
def RoleRecognizer(instance, created, **kwargs):
    user = Users.objects.get(username=instance.username)
    if instance.role == 1:
        group = Group.objects.get(name="")
    if instance.role == 2:
        group = Group.objects.get(name="")
    if instance.role == 3:
        group = Group.objects.get(name="")
    if instance.role == 4:
        group = Group.objects.get(name="")
    else:
        user.groups.add(group)
