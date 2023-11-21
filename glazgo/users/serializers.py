from rest_framework import serializers

from .models import *


class ULUSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]
