from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import UserRegistrationForm, PatientProfileForm
from accounts.models import User, PatientProfile


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('core:home')
    
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        patient_form = PatientProfileForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save(commit=False)
            user.role = 'PATIENT'
            user.save()
        
            patient_profile = patient_form.save(commit=False)
            patient_profile.user = user
            patient_profile.save()

            messages.success(request, 'Your account has been created successfully. You can now log in.')
            return redirect('core:login')
        else:
            for field,errors in user_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            for field,errors in patient_form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")    

    else:
        user_form = UserRegistrationForm()
        patient_form = PatientProfileForm()
    
    context = {
        'user_form': user_form,
        'patient_form': patient_form,
    }
    return render(request, 'core/register.html', context)



