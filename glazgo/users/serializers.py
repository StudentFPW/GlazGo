from rest_framework import serializers

from .models import *


class ULFSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class ULUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["username"]
