from django.db import models
from django.contrib.auth.models import models
from officialdata.models import Servicegroup, Designation, Sectiontype, Employeetype
from officedata.models import Office, Officetype
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Staff(models.Model):
    staffname_nepali = models.CharField(max_length= 150, verbose_name="नाम")
    staffname_english = models.CharField(max_length=150, verbose_name="Name")
    staff_id = models.CharField(max_length=20, verbose_name="कर्मचारी संकेत नं.")
    servicegroup_nepali = models.ForeignKey(Servicegroup, on_delete=models.CASCADE, verbose_name="सेवा समूह")
    designation_nepali = models.ForeignKey(Designation, on_delete=models.CASCADE, verbose_name="पद")
    Sectiontype_nepali = models.ForeignKey(Sectiontype, on_delete=models.CASCADE, verbose_name="शाखा")
    officetype_nepali = models.ForeignKey(Officetype, on_delete=models.CASCADE, verbose_name="कार्यरत कार्यालय")
    officename_nepali = models.ForeignKey(Office, on_delete=models.CASCADE, verbose_name="कार्यालय")
    citizenship_no = models.CharField(max_length=25, verbose_name="नागरिकता नं.")
    citizenship_dispatcheddate = models.DateField(verbose_name="जारी मिति")
    citizenship_dispatcheddistrict = models.CharField(max_length=50, verbose_name="जारी जिल्ला")
    # employeetype = models.ForeignKey(Employeetype, on_delete=models.CASCADE, verbose_name="कर्मचारी किसिम")
    # appointment_date = models.DateField(verbose_name="नियुक्ति मिति जस्तै: २०७७-०५-०५")
    # officeentry_date = models.DateField(verbose_name="कार्यालय प्रवेश मिति जस्तै: २०७७-०५-०५")


    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.staffname_nepali

    def get_absolute_url(self):
        return reverse('staff-list')