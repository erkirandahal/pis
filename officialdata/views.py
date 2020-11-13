from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DesignationCreateForm, EmployeeTypeCreateForm, SectionTypeCreateForm, ServiceGroupCreateForm
from .models import Designation, Employeetype, Sectiontype, Servicegroup
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from officedata.views import UserAccessMixin

class DesignationCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'officialdata.add_designation'
    form_class = DesignationCreateForm
    template_name = 'officialdata/designation_form.html'
    # success_url = '/designation/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DesignationListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'officialdata.view_designation'
    model = Designation
    template_name = 'designation/designation_list.html'


    # def get_queryset(self):
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Designation.objects.filter(author=user).order_by('-date_posted')

class DesignationDetailView(LoginRequiredMixin, UserAccessMixin, DetailView):
    permission_required = 'officialdata.view_designation'
    model = Designation
    context_object_name = 'designation'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_designation'] = self.model.objects.all()
        return context

class DesignationUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = 'officialdata.change_designation'
    model = Designation
    fields = ['designation_nepali', 'designation_english']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DesignationDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'officialdata.delete_designation'
    model = Designation
    success_url = '/designation/list/'

'''  --------------------------------------------------------------------------------------------------------
					Employee Type Addition Views Starts Here (स्थायी / Permanent, करार / Contract etc. 
-----------------------------------------------------------------------------------------------------------'''

class EmployeeTypeCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'officialdata.add_employeetype'
    form_class = EmployeeTypeCreateForm
    template_name = 'officialdata/employeetype_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EmployeeTypeListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'officialdata.view_employeetype'
    model = Employeetype
    template_name = 'employeetype/employeetype_list.html'

class EmployeeTypeUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = 'officialdata.change_employeetype'
    model = Employeetype
    fields = ['employeetype_nepali', 'employeetype_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EmployeeTypeDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'officialdata.delete_employeetype'
    model = Employeetype
    success_url = '/employeetype/list/'

'''  --------------------------------------------------------------------------------------------------------
					Section Type Views Starts Here 
-----------------------------------------------------------------------------------------------------------'''

class SectionTypeCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'officialdata.add_sectiontype'
    form_class = SectionTypeCreateForm
    template_name = 'officialdata/sectiontype_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class SectionTypeListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'officialdata.list_sectiontype'
    model = Sectiontype
    template_name = 'sectiontype/sectiontype_list.html'


class SectionTypeUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = 'officialdata.change_sectiontype'
    model = Sectiontype
    fields = ['sectiontype_nepali', 'sectiontype_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class SectionTypeDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'officialdata.delete_sectiontype'
    model = Sectiontype
    success_url = '/sectiontype/list/'


'''  --------------------------------------------------------------------------------------------------------
					Service Group Views Starts Here 
-----------------------------------------------------------------------------------------------------------'''

class ServiceGroupCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'officialdata.add_servicegroup'
    form_class = ServiceGroupCreateForm
    template_name = 'officialdata/servicegroup_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ServiceGroupListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'officialdata.list_servicegroup'
    model = Servicegroup
    template_name = 'servicegroup/servicegroup_list.html'

class ServiceGroupUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = 'officialdata.change_servicegroup'
    model = Servicegroup
    fields = ['servicegroup_nepali', 'servicegroup_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ServiceGroupDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'officialdata.delete_servicegroup'
    model = Servicegroup
    success_url = '/servicegroup/list/'


#GET MORE THAN ONE VIEW TO RENDER IN SINGLE PAGE,

class AllOfficialdataListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = ('officialdata.list_servicegroup', 'officialdata.list_designation', 'officialdata.list_sectiontype', 'officialdata.list_employeetype')
    template_name = 'officialdata/allofficialdata_list.html'
    queryset = Servicegroup.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AllOfficialdataListView, self).get_context_data(**kwargs)
        context['designation_list'] = Designation.objects.all()
        context['sectiontype_list'] = Sectiontype.objects.all()
        context['employeetype_list'] = Employeetype.objects.all()
        context['servicegroup_list'] = self.queryset
        return context