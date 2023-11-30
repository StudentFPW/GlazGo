import secrets

from rest_framework import serializers

from .models import ReferralRelationship, ReferralCode


class RRSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferralRelationship
        fields = ["employer", "employee", "refer_token"]


class RCSerializer(serializers.ModelSerializer):
    refer_relations = RRSerializer(many=True, default="")

    class Meta:
        model = ReferralCode
        fields = ["token", "user", "refer_relations"]
