from django import forms
from .models import Designation, Employeetype, Sectiontype

class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['designation_nepali', 'designation_english']

class EmployeeTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Employeetype
        fields = ['employeetype_nepali', 'employeetype_english']

class SectionTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Sectiontype
        fields = ['sectiontype_nepali', 'sectiontype_english']

