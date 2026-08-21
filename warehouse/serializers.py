from rest_framework import serializers
from .models import Part, StockOperation

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'

class StockOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOperation
        fields = '__all__'
        read_only_fields = ['id', 'part', 'created_at']