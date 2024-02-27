from django.db import models
from vendors.models import Vendor, PhoneNumber
from credits.models import CreditType

class CreditAddition(models.Model):
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='additions'
    )

    class Meta:
        verbose_name = 'Credit Addition'
        verbose_name_plural = 'Credit Additions'


class CreditSubtraction(models.Model):
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='subtractions'
    )
    phone_number = models.ForeignKey(
        PhoneNumber,
        on_delete=models.PROTECT,
        related_name='credit_purchases'
    )
    amount = models.ForeignKey(
        CreditType,
        on_delete=models.PROTECT,
        related_name='credit_purchases'
    )

    class Meta:
        verbose_name = 'Credit Subtraction'
        verbose_name_plural = 'Credit Subtractions'