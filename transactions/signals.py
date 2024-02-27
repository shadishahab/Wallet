from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CreditAddition

@receiver(post_save, sender=CreditAddition)
def update_vendor_balance_credit_addition(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            vendor = instance.vendor
            vendor.balance += instance.amount
            vendor.save()
