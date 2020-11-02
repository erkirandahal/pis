from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


'''  --------------------------------------------------------------------------------------------------------
                    Section (शाखा) Code Begins
-----------------------------------------------------------------------------------------------------------'''
class Section(models.Model):
    section_Nepali = models.CharField(max_length=100)
    section_English = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.section_Nepali
        return self.section_English

    def get_absolute_url(self):
        return reverse('section-list', kwargs={'pk': self.pk})
