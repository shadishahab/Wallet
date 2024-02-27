from django.shortcuts import get_object_or_404
from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from vendors.models import Vendor
from .serializers import CreditSubtractionCreateSerializer
from credits.models import CreditType

class CreditSubtractionCreateAPIView(generics.CreateAPIView):
    serializer_class = CreditSubtractionCreateSerializer

    def perform_create(self, serializer):
        amount_value = self.request.data.get('amount')
        vendor_id = self.request.user.vendor.id
        #vendor_id = self.kwargs.get('vendor_id')
        print(vendor_id)
        vendor = get_object_or_404(Vendor, pk=vendor_id)
        print(amount_value)
        credit_type = get_object_or_404(CreditType, pk=amount_value)
        if vendor.balance < credit_type.value:
            return Response({'error': 'Insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)
        with transaction.atomic():
            serializer.save(vendor=vendor, amount=credit_type)
            vendor.balance -= credit_type.value
            vendor.save()
        return Response({'success': True}, status=status.HTTP_201_CREATED)
