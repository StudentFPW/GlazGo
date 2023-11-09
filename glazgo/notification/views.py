from django.db.models import FilteredRelation, Q, F
from django.shortcuts import render
from pytz import exceptions
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializer import MyMessageSerializer


# функция получения кверисета непрочтенных сообщений адресованных текущему пользователю
def get_message(user):
    return Message.objects.filter(user_id=user, viewed=False)

class MyMessageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyMessageSerializer
    #permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        self.request.session['user_id'] = 2 # костыль для проверки, пока авторизации нет
        qs = get_message(self.request.session['user_id'])

        return qs
