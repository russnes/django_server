from rest_framework import serializers
from .models import *

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'

