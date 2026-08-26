from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = '__all__'
    read_only_fields = ['id', 'is_active', 'created_at']