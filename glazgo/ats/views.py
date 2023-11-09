from rest_framework import viewsets, mixins
from .models import Message
from .serializer import MyMessageSerializer


def get_message(user):
    """
    функция получения кверисета непрочтенных сообщений адресованных текущему пользователю
    """
    return Message.objects.filter(user_id=user, viewed=False)


class MyMessageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    Класс MyMessageViewSet представляет собой набор представлений, который извлекает набор сообщений для
    конкретного пользователя и присваивает его переменной qs.
    """

    serializer_class = MyMessageSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        self.request.session[
            "user_id"
        ] = 2  # костыль для проверки, пока авторизации нет
        print(f"Test: User {self.request.session['user_id']}")
        qs = get_message(self.request.session["user_id"])
        print(f"Test: Message {qs}")

        return qs
