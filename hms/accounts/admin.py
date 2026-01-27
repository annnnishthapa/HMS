from django.contrib import admin
from .models import User, DoctorProfile, PatientProfile, NurseProfile, ReceptionistProfile
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','role','is_active','is_staff')
    search_fields = ('username','email','role')
    list_filter = ('role','is_active','is_staff')
@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user','specialization','license_number','contact_number')
    search_fields = ('user__username','specialization','license_number')
@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = ('user','date_of_birth','address','emergency_contact')
    search_fields = ('user__username','address','emergency_contact')
@admin.register(NurseProfile)
class NurseProfileAdmin(admin.ModelAdmin):
    list_display = ('user','department','shift_timings','contact_number')
    search_fields = ('user__username','department','contact_number')

@admin.register(ReceptionistProfile)
class ReceptionistProfileAdmin(admin.ModelAdmin):
    list_display = ('user','desk_number','contact_number')
    search_fields = ('user__username','desk_number','contact_number')    