from django.contrib import admin
from .models import Designation, Employeetype, Sectiontype
# Register your models here.

admin.site.register(Designation)
admin.site.register(Employeetype)
admin.site.register(Sectiontype)