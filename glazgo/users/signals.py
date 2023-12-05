from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User
from .serializers import create_reftoken


@receiver(post_save, sender=User)
def Recognizer(instance, created, **kwargs):
    if created:
        if instance.is_superuser:
            User.objects.filter(pk=instance.pk).update(role=0)
            for i in range(100):
                create_reftoken(instance)
