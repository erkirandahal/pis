from django.db import models
from django.contrib.auth.models import models
from officialdata.models import Servicegroup, Designation, Sectiontype, Employeetype
from officedata.models import Office, Officetype
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from address.models import Province, LocalLevelType
# Create your models here.

class Staff(models.Model):
    author = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    staffname_nepali = models.CharField(max_length= 150, verbose_name="नाम")
    staffname_english = models.CharField(max_length=150, verbose_name="Name")
    staff_id = models.CharField(max_length=20, null=True, blank=True, verbose_name="कर्मचारी संकेत नं.")
    appointment_date = models.CharField(max_length=15, verbose_name="नियुक्ति मिति जस्तै: २०७७-०५-०५")
    officeentry_date = models.CharField(max_length=15, verbose_name="कार्यालय प्रवेश मिति जस्तै: २०७७-०५-०५")
    employeetype = models.ForeignKey(Employeetype, on_delete=models.CASCADE, verbose_name="कर्मचारी किसिम")
    servicegroup_nepali = models.ForeignKey(Servicegroup, on_delete=models.CASCADE, verbose_name="सेवा समूह")
    designation_nepali = models.ForeignKey(Designation, on_delete=models.CASCADE, verbose_name="पद")
    Sectiontype_nepali = models.ForeignKey(Sectiontype, on_delete=models.CASCADE, verbose_name="शाखा")
    officetype_nepali = models.ForeignKey(Officetype, on_delete=models.CASCADE, verbose_name="कार्यरत कार्यालय")
    officename_nepali = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name="कार्यालय")
    dob = models.CharField(max_length=15, verbose_name="जन्म मिति")
    citizenship_no = models.CharField(max_length=25, verbose_name="नागरिकता नं.")
    citizenship_dispatcheddate = models.CharField(max_length=15, verbose_name="जारी मिति")
    citizenship_dispatcheddistrict = models.CharField(max_length=50, verbose_name="जारी जिल्ला")
    grandfather_name = models.CharField(max_length=150, verbose_name="बाजे / ससुराको नाम")
    father_name = models.CharField(max_length=150, verbose_name="बाबुको नाम")
    mother_name = models.CharField(max_length=150, verbose_name="आमाको नाम")
    contact_no = models.CharField(max_length=10, verbose_name="सम्पर्क नं")
    email = models.CharField(max_length=150, null=True, blank=True, verbose_name="इमेल")
    permanentaddr_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='permanentaddr_province', verbose_name="प्रदेश")
    permanentaddr_district = models.CharField(max_length=150, verbose_name="जिल्ला")
    permanentaddr_locallevel = models.CharField(max_length=150, verbose_name="स्थानीय तह")
    permanentaddr_localleveltype = models.ForeignKey(LocalLevelType, on_delete=models.CASCADE, related_name='permanentaddr_localleveltype', verbose_name="स्थानीय तह प्रकार")
    permanentaddr_wardno = models.CharField(max_length=2, verbose_name="वडा नं.", default='2')
    temporaryaddr_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='temporaryaddr_province', verbose_name="प्रदेश")
    temporaryaddr_district = models.CharField(max_length=150, verbose_name="जिल्ला")
    temporaryaddr_locallevel = models.CharField(max_length=150, verbose_name="स्थानीय तह")
    temporaryaddr_localleveltype = models.ForeignKey(LocalLevelType, on_delete=models.CASCADE, related_name='temporaryaddr_localleveltype', verbose_name="स्थानीय तह प्रकार")
    temporaryaddr_wardno = models.CharField(max_length=2, verbose_name="वडा नं.", default='2')
    # citizenship_file = models.FileField(upload_to='staff/citizenship/')
    # appointment_file = models.FileField(upload_to='staff/appointment/')

    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='created_by')
    # staff_status = models.BooleanField(default=True, null=True, verbose_name="स्थिति")
    modified_date = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='modified_by')

    def __str__(self):
        return self.staffname_nepali

    # def get_absolute_url(self):
    #         return reverse('staff-list')

class StaffFiles(models.Model):
    citizenshipStaffFile = models.FileField(upload_to='staff/citizenship/', verbose_name="नागरिकता")
    appointmentStaffFile = models.FileField(upload_to='staff/appointment/', verbose_name="नियुक्ति पत्र")
    staffName = models.OneToOneField(Staff, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='created_by_stafffiles')
    modified_date = models.DateTimeField(default=timezone.now)
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='modified_by_stafffiles')
