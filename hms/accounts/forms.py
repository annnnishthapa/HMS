from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, DoctorProfile, PatientProfile, NurseProfile, ReceptionistProfile
from datetime import date


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your email  '}))
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your first name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your last name'})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter your password'})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget = forms.PasswordInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Confirm your password'})
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class PatientProfileForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
        ('OTHER', 'Other'),
        ('UNSPECIFIED', 'Unspecified'),
    ]
    gendwer = forms.ChoiceField(
        choices = GENDER_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control form-select-lg',})
      )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control form-control-lg',
            'type': 'date',
            'max': date.today().isoformat()})
    )
    
    
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-lg',
            'rows': 3,
            'placeholder': 'Enter your address'
        }))
    emergency_contact = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Enter emergency contact number'
        })
    )
    class Meta:
        model = PatientProfile
        fields = ['gender', 'date_of_birth', 'address', 'emergency_contact']