from django.db import models
from Encounter.models import Encounter
from accounts.models import PatientProfile

class BillingRecord(models.Model):
    appointment = models.OneToOneField(Encounter, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    billing_date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Billing Record for {self.patient.user.get_full_name()} - Amount: {self.amount} - Paid: {self.paid}"
