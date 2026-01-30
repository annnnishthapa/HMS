from django.contrib import admin
from .models import appointment

@admin.register(appointment)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'status')
    search_fields = ('patient__user__username', 'doctor__user__username')
    list_filter = ('status', 'priority', 'appointment_date')
    readonly_fields = ('created_at', 'updated_at')
