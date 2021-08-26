from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppTSSerializer
from .models import AppTS

# Create your views here.

class AppTSView(viewsets.ModelViewSet):
    serializer_class = AppTSSerializer
    queryset = AppTS.objects.all()