from django import forms
from .models import Staff
from officedata.models import Office, Officetype

class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staffname_nepali', 'staffname_english', 'staff_id', 'servicegroup_nepali', 'designation_nepali', 'Sectiontype_nepali',
                  'officetype_nepali', 'officename_nepali',
                  'citizenship_no', 'citizenship_dispatcheddate', 'citizenship_dispatcheddistrict']