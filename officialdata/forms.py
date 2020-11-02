from django import forms
from .models import Designation

class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['designation_nepali', 'designation_english']