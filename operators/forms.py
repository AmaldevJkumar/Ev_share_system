from django import forms
from .models import Maintenance, Relocation

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['notes']

class RelocationForm(forms.ModelForm):
    class Meta:
        model = Relocation
        fields = ['old_location', 'new_location']
