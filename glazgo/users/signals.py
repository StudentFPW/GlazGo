from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

from .models import *
from .serializers import create_reftoken


@receiver(post_save, sender=User)
def Recognizer(instance, **kwargs):
    if instance.is_superuser:
        User.objects.filter(pk=instance.pk).update(role=0)
        for i in range(100):
            create_reftoken(instance)
