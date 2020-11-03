from django.contrib import admin
from .models import Designation, Employeetype, Sectiontype, Servicegroup
# Register your models here.

admin.site.register(Designation)
admin.site.register(Employeetype)
admin.site.register(Sectiontype)
admin.site.register(Servicegroup)