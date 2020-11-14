from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import StaffCreateForm
from .models import Staff
from officedata.models import Officetype, Office
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from officedata.views import UserAccessMixin

class StaffCreateView(LoginRequiredMixin, CreateView):
    form_class = StaffCreateForm
    template_name = 'official/staff_form.html'
    # success_url = '/designation/list/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

# def load_officename(request):
#     officetype_nepali_id = request.GET.get('officetype_nepali_id')
#     officename_nepali = Office.objects.filter(officetype_nepali_id=officetype_nepali_id)
#     # return render(request, 'official/officename_dropdown_list_options.html', {'officename_nepali': officename_nepali})
#     print(list(officename_nepali.values('id', 'officename_nepali')))
#     return JsonResponse(list(officename_nepali.values('id', 'name')), safe=False)


class StaffListView(LoginRequiredMixin, ListView):
    model = Staff
    template_name = 'staff/staff_list.html'


class StaffUpdateView(LoginRequiredMixin, UpdateView):
    # permission_required = 'officialdata.change_servicegroup'
    model = Staff
    fields = ['staffname_nepali', 'staffname_english', 'staff_id',
              'appointment_date', 'officeentry_date',
              'employeetype', 'servicegroup_nepali', 'designation_nepali', 'Sectiontype_nepali',
              'officetype_nepali', 'officename_nepali',
              'dob', 'citizenship_no', 'citizenship_dispatcheddate', 'citizenship_dispatcheddistrict',
              'grandfather_name', 'father_name', 'mother_name',
              'contact_no', 'email',
              'permanentaddr_province', 'permanentaddr_district', 'permanentaddr_locallevel',
              'permanentaddr_localleveltype', 'permanentaddr_wardno',
              'temporaryaddr_province', 'temporaryaddr_district', 'temporaryaddr_locallevel',
              'temporaryaddr_localleveltype', 'temporaryaddr_wardno'
              ]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class StaffDetailView(DetailView):
	model = Staff

class OnlickPrint(DetailView):
	model = Staff