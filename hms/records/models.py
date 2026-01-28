from django.db import models
from accounts.models import PatientProfile, DoctorProfile , NurseProfile

class Ward(models.Model):
    name = models.CharField(max_length=100)
    floor = models.IntegerField()
    type = models.CharField(max_length=50)
    total_beds = models.IntegerField()

    def __str__(self):
        return self.name
    
class Bed(models.Model):
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name='beds')
    bed_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    class Meta:
        unique_together = ('ward', 'bed_number')
    def __str__(self):
        return f'Bed {self.bed_number} in {self.ward.name}'

#inpatient Admission
class Admission(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete = models.CASCADE , related_name='admissions')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True)
    bed = models.ForeignKey(Bed, on_delete=models.SET_NULL, null = True,blank=True)
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(blank=True, null=True)

    
    primary_diagnosis = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Admission of {self.patient.user.get_full_name()} on {self.admission_date.strftime("%Y-%m-%d %H:%M")}'

# Nurse Assignment
class NurseAssignment(models.Model):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE, related_name='nurse_assignments')
    nurse = models.ForeignKey(NurseProfile, on_delete=models.SET_NULL, null=True)
    
    start_at = models.DateTimeField()
    end_at = models.DateTimeField(blank=True , null=True)
    shift_choices = [
        ('MORN', 'Morning Shift'),
        ('NIGHT', 'Night Shift'),
        ('EVE', 'Evening Shift'),
         ]
    shift_type = models.CharField(max_length=10, choices=shift_choices)
    def __str__(self):
        return f'Nurse {self.nurse.user.get_full_name()} assigned to {self.admission.patient.user.get_full_name()}'
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.SET_NULL, null=True, related_name='created_records')
    nurse = models.ForeignKey(NurseProfile, on_delete=models.SET_NULL, null=True, related_name='assisted_records')
    diagnosis = models.TextField()
    treatment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Medical Record for {self.patient.user.get_full_name()} created on {self.date_created.strftime("%Y-%m-%d")}'

class PatientMedicalHistory(models.Model):
    patient = models.OneToOneField(PatientProfile, on_delete=models.CASCADE, related_name='medical_history')
    
    # Blood type
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
    ]
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    
    # Allergies (stored as text, comma-separated or JSON in production)
    allergies = models.TextField(blank=True, null=True, help_text="List patient allergies (medications, food, etc.)")
    
    # Chronic conditions
    chronic_conditions = models.TextField(blank=True, null=True, help_text="Ongoing medical conditions (diabetes, hypertension, etc.)")
    
    # Current medications
    current_medications = models.TextField(blank=True, null=True, help_text="List of current medications and dosages")
    
    # Past surgeries
    past_surgeries = models.TextField(blank=True, null=True, help_text="History of surgical procedures")
    
    personal_history = models.TextField(blank=True, null=True, help_text="if patient drinks alcohol, smokes, etc.")
    # Family medical history
    family_history = models.TextField(blank=True, null=True, help_text="Relevant family medical history")
    
    # Immunization records
    immunizations = models.TextField(blank=True, null=True, help_text="Vaccination history")
    
    # Additional notes
    notes = models.TextField(blank=True, null=True, help_text="Any additional medical history notes")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Medical History for {self.patient.user.get_full_name()}'
