from django.contrib import admin
from .models import BillingRecord

@admin.register(BillingRecord)
class BillingRecordAdmin(admin.ModelAdmin):
    list_display = ('encounter', 'amount', 'billing_date', 'paid')
    search_fields = ('encounter__patient__user__username', 'encounter__id')
    list_filter = ('paid', 'billing_date')
    readonly_fields = ('billing_date',)
    