from rest_framework import serializers
from .models import AppTS

class AppTSSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppTS
        fields = ('id', 'title', 'description', 'completed')