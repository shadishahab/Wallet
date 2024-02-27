from django.db import models

class CreditType(models.Model):
    value = models.PositiveIntegerField(unique=True)

    class Meta:
        verbose_name = 'Credit Type'
        verbose_name_plural = 'Credit Types'

    def __str__(self):
        return f"{self.value}"