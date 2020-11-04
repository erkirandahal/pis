from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Province(models.Model):
    provincename_nepali = models.CharField(max_length=50, verbose_name="प्रदेशको नाम")
    provincename_english = models.CharField(max_length=50, verbose_name="Province Name")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.provincename_nepali

    def get_absolute_url(self):
        return reverse('province-list')

class LocalLevelType(models.Model):
    localleveltypename_nepali = models.CharField(max_length=50, verbose_name="स्थानीय तहको किसिम")
    localleveltypename_english = models.CharField(max_length=50, verbose_name="Local Level Name")
    date_posted = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.localleveltypename_nepali

    def get_absolute_url(self):
        return reverse('localleveltype-list')