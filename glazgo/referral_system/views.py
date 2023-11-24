from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import ReferralRelationship, ReferralCode
from .serializers import *


class RRViewSet(viewsets.ModelViewSet):
    serializer_class = RRSerializer
    queryset = ReferralRelationship.objects.all()


class RCViewSet(viewsets.ModelViewSet):
    serializer_class = RCSerializer
    queryset = ReferralCode.objects.all()
