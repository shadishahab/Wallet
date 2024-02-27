from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class Vendor(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name='vendor')
    description = models.TextField(blank=True, max_length=128
    )
    balance = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'

    def __str__(self):
        return str(self.user)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    owner_name=models.CharField(blank=True, max_length=32)
    vendor = models.ForeignKey(
        Vendor,
        on_delete=models.CASCADE,
        related_name='phone_numbers'
    )

    class Meta:
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone Numbers'

    def __str__(self):
        return self.number