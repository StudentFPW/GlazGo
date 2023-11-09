from django.db.models import FilteredRelation, Q, F
from django.shortcuts import render
from pytz import exceptions
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializer import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    #permission_classes = (IsAuthenticated,)
