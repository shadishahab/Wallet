from django.contrib import admin
from .models import Vendor, PhoneNumber
from users.models import CustomUser

class PhoneNumberInLine(admin.TabularInline):
    model = PhoneNumber

class VendorAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user', 'balance', 'description']
    search_fields = ['user']
    list_filter = ['user']
    inlines = [PhoneNumberInLine]

    def user_id(self, obj):
        return obj.user.id
    user_id.short_description = 'user_id'

admin.site.register(CustomUser)
admin.site.register(Vendor, VendorAdmin)
