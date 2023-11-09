from rest_framework import viewsets, mixins

from .models import *
from .serializer import *


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()


class ResponsibilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = ResponsibilitiesSerializer
    queryset = Responsibilities.objects.all()


class RequirementsViewSet(viewsets.ModelViewSet):
    serializer_class = RequirementsSerializer
    queryset = Requirements.objects.all()


class VacancyViewSet(viewsets.ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()


class CandidatePromotionViewSet(viewsets.ModelViewSet):
    serializer_class = CandidatePromotionSerializer
    queryset = CandidatePromotion.objects.all()


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


# def get_message(user):
#     """
#     функция получения кверисета непрочтенных сообщений адресованных текущему пользователю
#     """
#     return Message.objects.filter(user_id=user, viewed=False)


# class MyMessageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
#     """
#     Класс MyMessageViewSet представляет собой набор представлений, который извлекает набор сообщений для
#     конкретного пользователя и присваивает его переменной qs.
#     """

#     serializer_class = MyMessageSerializer

#     def get_queryset(self):
#         # костыль для проверки, пока авторизации нет
#         self.request.session["user_id"] = 2

#         print(f"Test: User {self.request.session['user_id']}")

#         qs = get_message(self.request.session["user_id"])

#         print(f"Test: Message {qs}")

#         return qs
