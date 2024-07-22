# serializers.py
from rest_framework import serializers
from .models import JarCount

class JarCountSerializer(serializers.ModelSerializer):
    inventory_name = serializers.CharField(source='inventory.product_name', read_only=True)

    class Meta:
        model = JarCount
        fields = ['id', 'count', 'shift', 'timestamp']