from django.db import models
from accounts.models import User, DoctorProfile, PatientProfile

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('INITIAL', 'Initial'),
        ('FOLLOWUP', 'Follow-up'),
        ('EMERGENCY', 'Emergency'),
        ('ROUTINE', 'Routine Check-up'),
    ]

STATUS_CHOICES = [
    ('SCHEDULED', 'Scheduled'),
    ('COMPLETED', 'Completed'),
    ('CANCELLED', 'Cancelled'),
    ('COMPLETE', 'Completed'),
    ('NO_SHOW', 'No Show'),
]

PRIORITY_CHOICES = [
    ('NORMAL', 'Normal'),
    ('URGENT', 'Urgent'),
    ('EMERGENCY', 'Emergency'),
]

patient = models.ForeignKey(PatientProfile, on_delete= models.CASCADE, related_name='appointments')
doctor = models.ForeignKey(DoctorProfile, on_delete= models.CASCADE, related_name='appointments')

appointment_date = models.DateTimeField()
appointment_time = models.TimeField()
appointment_type = models.CharField(max_length=15, choices=STATUS_CHOICES, default='ROUTINE')

status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SCHEDULED')
priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='NORMAL')

notes = models.TextField(blank=True, null=True)

created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    ordering = ['appointment_date','appointment_time']
    unique_together = ('doctor', 'appointment_date','appointment_time')
    
def __str__(self):
    return f"{self.patient.user.get_full_name()} with Dr. {self.docotor.user.get_full_name()} on {self.appointment_date } " 
