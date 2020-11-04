from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Officetype(models.Model):
    officetype_nepali = models.CharField(max_length=70, verbose_name="कार्यालयको किसिम")
    officetype_english = models.CharField(max_length=70, verbose_name="Office Type")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.officetype_nepali

    def get_absolute_url(self):
        return reverse('officetype-list')

class Office(models.Model):
    WARD_NO = (
        ("१", "१"),
        ("२", "२"),
        ("३", "३"),
        ("४", "४"),
        ("५", "५"),
        ("६", "६"),
        ("७", "७"),
        ("८", "८"),
        ("९", "९"),
    )

    officename_nepali = models.CharField(max_length=100, verbose_name="कार्यालयको नाम")
    officename_english = models.CharField(max_length=100, verbose_name="Office Name")
    officeaddress = models.CharField(max_length=100, verbose_name="कार्यालयको ठेगाना")
    officetype = models.ForeignKey(Officetype, on_delete=models.CASCADE, null=True, verbose_name="कार्यालयको प्रकार")
    office_wardno = models.CharField(max_length=1, choices=WARD_NO, default=1, verbose_name="वडा नं.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.officename_nepali

    def get_absolute_url(self):
        return reverse('office-list')