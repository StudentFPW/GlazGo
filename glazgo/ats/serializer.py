from rest_framework import serializers

from .models import Message, Candidate
from .serializer import CandidateSerializer

class MyMessageSerializer(serializers.ModelSerializer):
    candidate_id = CandidateSerializer(required=False)

    class Meta:
        model = Message
        fields = ('candidate_id', 'viewed')

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = '__all__'
