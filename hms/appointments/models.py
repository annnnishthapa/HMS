from django.db import models
from django.utils import timezone
from accounts.models import User, DoctorProfile, PatientProfile

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('NO_SHOW', 'No Show'),
    ]
    APPOINTMENT_TYPE_CHOICES = [
        ('ROUTINE', 'Routine Check-up'),
        ('FOLLOW_UP', 'Follow-up'),
        ('EMERGENCY', 'Emergency Visit'),
    ]
    PRIORITY_CHOICES = [
        ('NORMAL', 'Normal'),
        ('URGENT', 'Urgent'),
        ('EMERGENCY', 'Emergency'),
    ]

    encounter = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, related_name='appointments')

    appointment_date = models.DateTimeField()
    appointment_time = models.TimeField(blank=True, null=True)
    appointment_type = models.CharField(max_length=15, choices=APPOINTMENT_TYPE_CHOICES, default='ROUTINE')

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='SCHEDULED')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='NORMAL')

    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['appointment_date', 'appointment_time']
        unique_together = ('doctor', 'appointment_date', 'appointment_time')
    
    def __str__(self):
        return f"{self.patient.user.get_full_name()} with Dr. {self.doctor.user.get_full_name()} on {self.appointment_date}"