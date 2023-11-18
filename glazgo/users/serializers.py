from rest_framework import serializers

from .models import *


class ULFSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ULUSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
