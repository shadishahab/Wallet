from django.contrib import admin
from .models import CreditType

class CreditTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'value']

admin.site.register(CreditType, CreditTypeAdmin)