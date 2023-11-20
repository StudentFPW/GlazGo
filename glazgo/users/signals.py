from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User)
def RoleRecognizer(instance, **kwargs):
    if not instance.is_superuser:
        user = User.objects.get(id=instance.pk)
        if instance.role == 1:
            group = Group.objects.get(name="UR")
        if instance.role == 2:
            group = Group.objects.get(name="URA")
        if instance.role == 3:
            group = Group.objects.get(name="UC")
        if instance.role == 4:
            group = Group.objects.get(name="UCA")
        user.groups.add(group)
        user.save()
    User.objects.filter(id=instance.pk).update(role=0)
