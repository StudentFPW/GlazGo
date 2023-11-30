from django.db import models
from django.conf import settings


class Conversation(models.Model):
    """
    Класс Conversation представляет разговор между двумя пользователями с инициатором и получателем и
    включает время начала.
    """

    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="convo_starter",
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="convo_participant",
    )
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    """
    Класс Message представляет сообщение, отправленное пользователем в беседе, с полями для отправителя,
    текста, вложения, идентификатора беседы и метки времени.
    """

    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="message_sender",
    )
    text = models.CharField(max_length=200, blank=True)
    attachment = models.FileField(blank=True)
    conversation_id = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-timestamp",)
