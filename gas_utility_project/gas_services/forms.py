from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        # fields = ['customer','request_date', 'status']  # Add other fields here
        exclude = ['request_date']
