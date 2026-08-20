from rest_framework import serializers
from .models import Part, StockOperation

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = ['id', 'name', 'category', 'quantity', 'description']

class StockOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockOperation
        fields = [
            'id', 
            'part', 
            'operation_type', 
            'quantity', 
            'performed_by',
            'recipient',
            'created_at'
        ]