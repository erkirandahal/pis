from django import forms
from .models import Officetype

class OfficeTypeCreateForm(forms.ModelForm):
    class Meta:
        model = Officetype
        fields = ['officetype_nepali', 'officetype_english']