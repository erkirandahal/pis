from django import forms
from .models import Province, LocalLevelType

class ProvinceCreateForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['provincename_nepali', 'provincename_english']

class LocalLevelTypeCreateForm(forms.ModelForm):
    class Meta:
        model = LocalLevelType
        fields = ['localleveltypename_nepali', 'localleveltypename_english']