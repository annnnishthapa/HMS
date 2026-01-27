from django.contrib import admin
from .models import Encounter

@admin.register(Encounter)
class EncounterAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'encounter_date', 'encounter_type', 'status', 'admission_decision')
    search_fields = ('patient__user__username', 'doctor__user__username', 'reason_for_visit')
    list_filter = ('encounter_type', 'status', 'admission_decision', 'encounter_date')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Participants', {
            'fields': ('doctor', 'patient', 'encounter_date')
        }),
        ('Encounter Info', {
            'fields': ('encounter_type', 'reason_for_visit')
        }),
        ('Clinical Details', {
            'fields': ('assessment', 'diagnosis', 'admission_decision')
        }),
        ('Status', {
            'fields': ('status', 'created_at', 'updated_at')
        }),
    )
