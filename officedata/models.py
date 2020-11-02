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
        return self.officename_nepali

    def get_absolute_url(self):
        return reverse('officetype-list')