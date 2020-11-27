from django import forms
from .models import Staff, StaffFiles
from officedata.models import Office, Officetype
from address.models import Province, LocalLevelType

class StaffCreateForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staffname_nepali', 'staffname_english', 'staff_id',
                  'appointment_date', 'officeentry_date',
                  'employeetype', 'servicegroup_nepali', 'designation_nepali', 'Sectiontype_nepali',
                  'officetype_nepali', 'officename_nepali',
                  'dob', 'citizenship_no', 'citizenship_dispatcheddate', 'citizenship_dispatcheddistrict',
                  'grandfather_name', 'father_name', 'mother_name',
                  'contact_no', 'email',
                  'permanentaddr_province', 'permanentaddr_district', 'permanentaddr_locallevel', 'permanentaddr_localleveltype', 'permanentaddr_wardno',
                  'temporaryaddr_province', 'temporaryaddr_district', 'temporaryaddr_locallevel',
                  'temporaryaddr_localleveltype', 'temporaryaddr_wardno',
                  ]

class StaffFileCreateForm(forms.ModelForm):
    class Meta:
        model = StaffFiles
        fields = ['citizenshipStaffFile', 'appointmentStaffFile',
            ]