from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .serializers import *

class TestModelViewSet(viewsets.ModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

