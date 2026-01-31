from django import forms
from .models import PatientMedicalHistory

class PatientMedicalHistoryForm(forms.ModelForm):

    class Meta:
        model = PatientMedicalHistory
        fields = ['patient', 'allergies', 'current_medications', 'chronic_conditions', 'family_history', 'personal_history', 'immunizations', 'past_surgeries']

        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control form-select-lg'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'current_medications': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'chronic_conditions': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'family_history': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'personal_history': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'immunizations': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'past_surgeries': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        }