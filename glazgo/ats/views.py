from datetime import timedelta

from django.utils.timezone import now
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

def get_message(user):
    """
    функция получения кверисета непрочтенных сообщений адресованных текущему пользователю
    """
    return Message.objects.filter(user_id__username=user, viewed=False)


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "user_id",
        "candidate_id",
    ]

    def get_queryset(self):

        print(f"Test: User {self.request.user}")

        qs = get_message(self.request.user)

        print(f"Test: Message {qs}")

        return qs

# Пункт 3 ТЗ. Поучение списка кандидатов, находящиеся на статусе более 1 дня

class WaitingCandidateViewSet(viewsets.ModelViewSet):
    serializer_class = WaitingCandidateSerializer
    queryset = CandidatePromotion.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "candidat_id",
        "status_change",
    ]

# отбираю кандидатов по фильтру: 1) сотрудник ведущий вакансию = текущий пользователь, кандидат еще не одобрен, статус пррисвоен более 1 дня назад
    def get_queryset(self):

        print(f"Test: User {self.request.user}")

        qs = CandidatePromotion.objects.filter(vacancy_id__customer__username=self.request.user,
                                               agreed=False,
                                               status_change_date__lt=now() - timedelta(days=1))

        print(f"Test: Message {qs}")

        return qs

# class MyMessageViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
#     """
#     Класс MyMessageViewSet представляет собой набор представлений, который извлекает набор сообщений для
#     конкретного пользователя и присваивает его переменной qs.
#     """
#
#     serializer_class = MessageSerializer


