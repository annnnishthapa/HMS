from django.contrib import admin
from .models import BillingRecord

@admin.register(BillingRecord)
class BillingRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'amount', 'billing_date', 'paid')
    search_fields = ('patient__user__username', 'encounter__id')
    list_filter = ('paid', 'billing_date')
    readonly_fields = ('billing_date',)
