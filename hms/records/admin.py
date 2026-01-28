from django.contrib import admin
from .models import Ward, Bed, Admission, NurseAssignment, MedicalRecord, PatientMedicalHistory

@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'type', 'total_beds')
    search_fields = ('name', 'type')
    list_filter = ('floor', 'type')

@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('bed_number', 'ward', 'is_occupied')
    search_fields = ('bed_number', 'ward__name')
    list_filter = ('is_occupied', 'ward')

@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'bed', 'admission_date', 'discharge_date')
    search_fields = ('patient__user__username', 'doctor__user__username')
    list_filter = ('admission_date', 'discharge_date')
    readonly_fields = ('admission_date',)

@admin.register(NurseAssignment)
class NurseAssignmentAdmin(admin.ModelAdmin):
    list_display = ('nurse', 'admission', 'shift_type', 'start_at', 'end_at')
    search_fields = ('nurse__user__username', 'admission__patient__user__username')
    list_filter = ('shift_type', 'start_at')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'nurse', 'date_created')
    search_fields = ('patient__user__username', 'doctor__user__username', 'diagnosis')
    list_filter = ('date_created', 'last_updated')
    readonly_fields = ('date_created', 'last_updated')

@admin.register(PatientMedicalHistory)
class PatientMedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'blood_type', 'created_at', 'updated_at')
    search_fields = ('patient__user__username', 'allergies', 'chronic_conditions')
    list_filter = ('blood_type', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Patient', {
            'fields': ('patient',)
        }),
        ('Basic Info', {
            'fields': ('blood_type',)
        }),
        ('Medical Conditions', {
            'fields': ('allergies', 'chronic_conditions', 'current_medications')
        }),
        ('History', {
            'fields': ('past_surgeries', 'family_history', 'immunizations')
        }),
        ('Additional Notes', {
            'fields': ('personal_history', 'notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
