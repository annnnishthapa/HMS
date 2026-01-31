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
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, null= True)
    def __str__(self):
        return self.username
    

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    contact_number = models.CharField(max_length=15)
    department_options = [
        ('EMERGENCY MEDICINE', 'Emergency Medicine'),
        ('INTERNAL MEDICINE', 'Internal Medicine'),
        ('FAMILY MEDICINE', 'Family Medicine'),
        ('PEDIATRICS', 'Pediatrics'),
        ('OBSTETRICS & GYNECOLOGY', 'Obstetrics & Gynecology'),
        ('SURGERY', 'Surgery'),
        ('ORTHOPEDICS', 'Orthopedics'),
        ('CARDIOLOGY', 'Cardiology'),
        ('NEUROLOGY', 'Neurology'),
        ('PSYCHIATRY', 'Psychiatry'),
        ('DERMATOLOGY', 'Dermatology'),
        ('OPHTHALMOLOGY', 'Ophthalmology'),
        ('ENT', 'Ear, Nose, and Throat (ENT)'),
        ('RADIOLOGY', 'Radiology'),
        ('ANESTHESIOLOGY', 'Anesthesiology'),
        ('ONCOLOGY', 'Oncology'),
        ('GASTROENTEROLOGY', 'Gastroenterology'),
        ('NEPHROLOGY', 'Nephrology'),
        ('PULMONOLOGY', 'Pulmonology'),
        ('UROLOGY', 'Urology'),
        ('ENDROCRINOLOGY', 'Endocrinology'),
        ('INFECTIOUS DISEASES', 'Infectious Diseases'),
        ('RHEUMATOLOGY', 'Rheumatology'),
        ('HEMATOLOGY', 'Hematology'),
        ('PATHOLOGY', 'Pathology'),
        ('OTHER', 'Other'),

    ]
    department = models.CharField(max_length=50, choices=department_options, default='OTHER')
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialization}"


class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('OTHER', 'Other'),
        ('UNSPECIFIED', 'Unspecified'),
    ]
    gender = models.CharField(max_length=12, choices=GENDER_CHOICES, default='UNSPECIFIED')
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact = models.CharField(max_length=15)
    def __str__(self):
        return self.user.get_full_name()


class NurseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    shift_timings = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Nurse {self.user.get_full_name()}"
class ReceptionistProfile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    desk_number = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    def __str__(self):
        return f"Receptionist {self.user.get_full_name()}"