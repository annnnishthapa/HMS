from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES  = [
        ('ADMIN', 'Admin'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
        ('PATIENT', 'Patient'),
        ('RECEPTIONIST', 'Receptionist'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='PATIENT')

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    contact_number = models.CharField(max_length=15)

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)


class NurseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    shift_timings = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

class ReceptionistProfile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    desk_number = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)