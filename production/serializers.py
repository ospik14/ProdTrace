from rest_framework import serializers
from .models import DroneModels, Drone, ProductionStages

class DroneModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneModels
        fields = '__all__'
        read_only_fields = ['id']

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

class StagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionStages
        fields = '__all__'
        read_only_fields = ['id']