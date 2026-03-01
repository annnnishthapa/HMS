from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import DoctorProfile, PatientProfile
from appointments.forms import AppointmentForm
from appointments.models import Appointment


@login_required
def appointment_list(request):
	if request.user.role == 'PATIENT':
		appointments = Appointment.objects.filter(patient__user=request.user)
	elif request.user.role == 'DOCTOR':
		appointments = Appointment.objects.filter(doctor__user=request.user)
	else:
		appointments = Appointment.objects.all()

	context = {
		'appointments': appointments,
	}
	return render(request, 'appointments/appointment_list.html', context)


@login_required
def create_appointment(request):
	try:
		patient = PatientProfile.objects.get(user=request.user)
	except PatientProfile.DoesNotExist:
		messages.error(request, 'Only patients can create appointments from this page.')
		return redirect('core:home')

	initial_data = {
		'gender': patient.gender,
		'date_of_birth': patient.date_of_birth,
		'address': patient.address,
		'emergency_contact': patient.emergency_contact,
	}

	if request.method == 'POST':
		form = AppointmentForm(request.POST)
		if form.is_valid():
			appointment = form.save(commit=False)
			appointment.patient = patient
			appointment.save()

			patient.gender = form.cleaned_data.get('gender') or patient.gender
			patient.date_of_birth = form.cleaned_data.get('date_of_birth') or patient.date_of_birth
			patient.address = form.cleaned_data.get('address') or patient.address
			patient.emergency_contact = form.cleaned_data.get('emergency_contact') or patient.emergency_contact
			patient.save()

			messages.success(request, 'Appointment created successfully.')
			return redirect('core:home')
	else:
		form = AppointmentForm(initial=initial_data)

	context = {
		'form': form,
	}
	return render(request, 'appointments/create_appointment.html', context)
