from rest_framework import serializers
from .models import Message
from ats.serializer import CandidateSerializer


class MyMessageSerializer(serializers.ModelSerializer):
    candidate_id = CandidateSerializer(required=False)

    class Meta:
        model = Message
        fields = ('candidate_id', 'viewed')