from django import forms
from .models import Designation, Employeetype

class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['designation_nepali', 'designation_english']

class EmployeeTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Employeetype
        fields = ['employeetype_nepali', 'employeetype_english']