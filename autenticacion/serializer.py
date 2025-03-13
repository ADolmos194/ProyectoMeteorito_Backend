from rest_framework import serializers
from .models import Loginusuarios 

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
