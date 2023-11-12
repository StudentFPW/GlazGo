from rest_framework import viewsets, generics, filters, mixins
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializer import *


class CPHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = CPHistorySerializer
    queryset = CPHistory.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "candidat_id",
        "vacancy_id",
        "recruter_id",
        "status",
        "datetime",
    ]


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "company_name",
        "mailing_address",
        "phone",
        "email",
    ]


class ResponsibilitiesViewSet(viewsets.ModelViewSet):
    serializer_class = ResponsibilitiesSerializer
    queryset = Responsibilities.objects.all()


class RequirementsViewSet(viewsets.ModelViewSet):
    serializer_class = RequirementsSerializer
    queryset = Requirements.objects.all()


class VacancyViewSet(viewsets.ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "recruter",
        "customer",
        "status_vacancy",
        "salary2",
    ]


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "user_id",
        "phone",
    ]


class CPromotionViewSet(viewsets.ModelViewSet):
    serializer_class = CPromotionSerializer
    queryset = CandidatePromotion.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "candidat_id",
        "status_change",
    ]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "user_id",
        "candidate_id",
    ]


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
