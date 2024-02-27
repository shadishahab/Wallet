from .models import CreditSubtraction
from rest_framework import serializers

class CreditSubtractionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditSubtraction
        fields = ['phone_number', 'amount']