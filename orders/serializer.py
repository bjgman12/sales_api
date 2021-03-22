from rest_framework import serializers
from .models import Orders

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','owner', 'specail_instructions','price','created_at')
        model = Orders