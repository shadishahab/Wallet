from django.contrib import admin
from .models import CreditAddition, CreditSubtraction

class CreditAdditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor', 'amount', 'timestamp']
    search_fields = ['id', 'vendor', 'amount', 'timestamp']
    list_filter = ['vendor']

class CreditSubtractionAdmin(admin.ModelAdmin):
    list_display = ['id', 'vendor', 'amount', 'timestamp', 'phone_number']
    search_fields = ['id', 'vendor', 'amount', 'timestamp', 'phone_number']
    list_filter = ['vendor', 'amount', 'phone_number']

admin.site.register(CreditAddition, CreditAdditionAdmin)
admin.site.register(CreditSubtraction, CreditSubtractionAdmin)