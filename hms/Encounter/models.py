from accounts.models import DoctorProfile, PatientProfile                                                  
from django.db import models


class Encounter(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete= models.SET_NULL, null=True)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    encounter_date = models.DateTimeField()
    reason_for_visit = models.TextField()
    ENCOUNTER_TYPE_CHOICES = [
        ('OUTPATIENT', 'Outpatient'),
        ('EMERGENCY', 'Emergency'),
        ('FOLLOWUP', 'Follow-up'),
    ]
    encounter_type = models.CharField(max_length=15, choices=ENCOUNTER_TYPE_CHOICES, default='OUTPATIENT')
    assessment = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)

    ADMISSION_DECISIONS = [
        ('DISCHARGE', 'Discharge'),
        ('ADMIT', 'Admit'),
        ('OBSERVE', 'Observe(4-6 hours)'),
    ]
    admission_decision = models.CharField(max_length=10, choices=ADMISSION_DECISIONS, blank=True, null=True)
    status = models.CharField(max_length=10, choices =[
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ], default='SCHEDULED')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Encounter of {self.patient.user.get_full_name()} with Dr. {self.doctor.user.get_full_name()} on {self.encounter_date.strftime('%Y-%m-%d %H:%M')}"
    
