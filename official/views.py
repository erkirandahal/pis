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
from django.urls import reverse_lazy,reverse

class StaffCreateView(LoginRequiredMixin, CreateView):
    form_class = StaffCreateForm
    template_name = 'official/staff_form.html'
    success_url = '/staff/list/'

    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.instance.created_by = self.request.user
        else:
            form.instance.author = self.request.user
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
    context_object_name = 'staff'

    def test_func(self):
        superuser = self.get_object()
        if self.request.user == self.request.user.is_superuser:
            return True
        return False

class StaffUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # permission_required = 'officialdata.change_servicegroup'
    model = Staff
    # success_url = '/staff/'
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
        if self.request.user.is_superuser:
            form.instance.modified_by = self.request.user
        else:
            form.instance.modified_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_superuser:
            return reverse_lazy('staff-list')
        else:
            return reverse_lazy('staff-post', kwargs={'username': self.request.user})

        return super(StaffUpdateView, self).get_success_url()

    def test_func(self):
        staff = self.get_object()
        if self.request.user == staff.author or self.request.user.is_superuser:
            return True
        return False

class StaffDetailView(DetailView):
	model = Staff


class UserPostListView(LoginRequiredMixin, ListView):
	model = Staff
	template_name = 'official/user_post.html'
	context_object_name = 'staff'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Staff.objects.filter(author=user)

# class UserStaffUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     # permission_required = 'officialdata.change_servicegroup'
#     model = Staff
#     success_url = '/staff/'
#     fields = ['staffname_nepali', 'staffname_english', 'staff_id',
#               'appointment_date', 'officeentry_date',
#               'employeetype', 'servicegroup_nepali', 'designation_nepali', 'Sectiontype_nepali',
#               'officetype_nepali', 'officename_nepali',
#               'dob', 'citizenship_no', 'citizenship_dispatcheddate', 'citizenship_dispatcheddistrict',
#               'grandfather_name', 'father_name', 'mother_name',
#               'contact_no', 'email',
#               'permanentaddr_province', 'permanentaddr_district', 'permanentaddr_locallevel',
#               'permanentaddr_localleveltype', 'permanentaddr_wardno',
#               'temporaryaddr_province', 'temporaryaddr_district', 'temporaryaddr_locallevel',
#               'temporaryaddr_localleveltype', 'temporaryaddr_wardno'
#               ]
#
#     def form_valid(self, form):
#         if self.request.user.is_superuser:
#             form.instance.modified_by = self.request.user
#         else:
#             form.instance.modified_by = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         staff = self.get_object()
#         if self.request.user == staff.author or self.request.user.is_superuser:
#             return True
#         return False