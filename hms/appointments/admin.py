from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('encounter', 'doctor', 'appointment_date', 'status')
    search_fields = ('encounter__patient__user__username', 'doctor__user__username')
    list_filter = ('status', 'priority', 'appointment_date')
    readonly_fields = ('created_at', 'updated_at')
