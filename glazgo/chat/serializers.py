from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Класс MessageSerializer является сериализатором модели Message, за исключением поля conversation_id.
    """

    class Meta:
        model = Message
        exclude = ("conversation_id",)


class ConversationListSerializer(serializers.ModelSerializer):
    """
    Класс ConversationListSerializer — это сериализатор, который сериализует объекты Conversation,
    включая инициатора, получателя и последнее сообщение.
    """

    initiator = UserSerializer()
    receiver = UserSerializer()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ["initiator", "receiver", "last_message"]

    def get_last_message(self, instance):
        message = instance.message_set.first()
        if message:
            return MessageSerializer(instance=message).data
        else:
            return None


class ConversationSerializer(serializers.ModelSerializer):
    """
    Класс ConversationSerializer используется для сериализации объектов Conversation, включая
    инициатора, получателя и список сообщений.
    """

    initiator = UserSerializer()
    receiver = UserSerializer()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ["initiator", "receiver", "message_set"]
