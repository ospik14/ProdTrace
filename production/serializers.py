from rest_framework import serializers
from .models import DroneModels

class DroneModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneModels
        fields = '__all__'
        read_only_fields = ['id']