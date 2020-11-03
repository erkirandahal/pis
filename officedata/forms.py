from django import forms
from .models import Officetype, Office

class OfficeTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Officetype
        fields = ['officetype_nepali', 'officetype_english']

class OfficeCreateForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['officename_nepali', 'officename_english', 'officeaddress', 'officetype']
