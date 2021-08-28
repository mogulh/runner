from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import *

class RunStampSerializer(serializers.ModelSerializer):
    speed = ReadOnlyField()
    distance = ReadOnlyField()
    class Meta:
        model=RunStamp
        fields = "__all__"


class RunSerializer(serializers.ModelSerializer):
    speed = ReadOnlyField()
    duration = ReadOnlyField()
    class Meta:
        model=Run
        fields = "__all__"


