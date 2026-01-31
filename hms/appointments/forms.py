from django import forms
from appointments.models import Appointment
from accounts.models import PatientProfile

class AppointmentForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices = PatientProfile.GENDER_CHOICES,
        required = False,
        widget = forms.Select(attrs={'class': 'form-control form-select-lg'})
    )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}))                           

    address = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'})
    )
    emergency_contact = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    class Meta:
        model = Appointment
        fields = ['doctor','appointment_date','appointment_time','appointment_type','priority','notes']

        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'datetime-local', 'class': 'form-control form-control-lg'}),
            'appointment_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control form-control-lg'}),
            'appointment_type': forms.Select(attrs={'class': 'form-control form-select-lg'}),
            'notes': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'priority': forms.Select(attrs={'class': 'form-control form-select-lg'}),
            'doctor': forms.Select(attrs={'class': 'form-control form-select-lg'}),            
        }
