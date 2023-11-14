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
        "user_id",
        "company_name",
        "mailing_address",
        "phone",
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
        "email",
        "phone",
        "birthday",
    ]


class CPromotionViewSet(viewsets.ModelViewSet):
    serializer_class = CPromotionSerializer
    queryset = CandidatePromotion.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "candidat_id",
        "vacancy_id",
        "recruter_id",
        "status_change",
        "status_change_date",
    ]


class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "user_id",
        "candidate_id",
        "viewed",
    ]
