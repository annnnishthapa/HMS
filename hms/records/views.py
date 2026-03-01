from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from accounts.models import PatientProfile
from records.forms import PatientMedicalHistoryForm
from records.models import PatientMedicalHistory


@login_required
def medical_history_list(request):
	if request.user.role == 'PATIENT':
		histories = PatientMedicalHistory.objects.filter(patient__user=request.user)
	else:
		histories = PatientMedicalHistory.objects.select_related('patient', 'patient__user').all()

	context = {
		'histories': histories,
	}
	return render(request, 'records/medical_history_list.html', context)


@login_required
def medical_history_form(request):
	is_patient_user = request.user.role == 'PATIENT'

	if is_patient_user:
		try:
			patient_profile = PatientProfile.objects.get(user=request.user)
		except PatientProfile.DoesNotExist:
			messages.error(request, 'Patient profile was not found for this account.')
			return redirect('core:home')
	else:
		patient_profile = None

	if request.method == 'POST':
		post_data = request.POST.copy()
		if is_patient_user:
			post_data['patient'] = str(patient_profile.id)

		form = PatientMedicalHistoryForm(post_data)
		if is_patient_user:
			form.fields['patient'].queryset = PatientProfile.objects.filter(id=patient_profile.id)

		if form.is_valid():
			selected_patient = form.cleaned_data['patient']
			history, _ = PatientMedicalHistory.objects.get_or_create(patient=selected_patient)

			history.allergies = form.cleaned_data['allergies']
			history.current_medications = form.cleaned_data['current_medications']
			history.chronic_conditions = form.cleaned_data['chronic_conditions']
			history.family_history = form.cleaned_data['family_history']
			history.personal_history = form.cleaned_data['personal_history']
			history.immunizations = form.cleaned_data['immunizations']
			history.past_surgeries = form.cleaned_data['past_surgeries']
			history.save()

			messages.success(request, 'Medical history saved successfully.')
			return redirect('core:home')
	else:
		initial_data = {}
		if is_patient_user:
			initial_data['patient'] = patient_profile.id

		form = PatientMedicalHistoryForm(initial=initial_data)
		if is_patient_user:
			form.fields['patient'].queryset = PatientProfile.objects.filter(id=patient_profile.id)

	context = {
		'form': form,
		'is_patient_user': is_patient_user,
	}
	return render(request, 'records/medical_history_form.html', context)
