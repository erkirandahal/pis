from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Designation(models.Model):
    designation_nepali = models.CharField(max_length=100)
    designation_english = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.designation_nepali

    def get_absolute_url(self):
        return reverse('designation-list')

class Employeetype(models.Model):
    employeetype_nepali = models.CharField(max_length=70, verbose_name="कर्मचारी किसिम")
    employeetype_english = models.CharField(max_length=70, verbose_name="Employee Type")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.employeetype_nepali

    def get_absolute_url(self):
        return reverse('employeetype-list')

class Sectiontype(models.Model):
    sectiontype_nepali = models.CharField(max_length=70, verbose_name="शाखाको नाम")
    sectiontype_english = models.CharField(max_length=70, verbose_name="Section Name")
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.sectiontype_nepali

    def get_absolute_url(self):
        return reverse('sectiontype-list')