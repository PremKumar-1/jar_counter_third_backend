# serializers.py
from rest_framework import serializers
from .models import JarCount

class JarCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarCount
        fields = ['id', 'count', 'shift', 'timestamp']