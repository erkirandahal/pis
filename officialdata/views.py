from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DesignationCreateForm, EmployeeTypeCreateForm
from .models import Designation, Employeetype
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,)

class DesignationCreateView(LoginRequiredMixin, CreateView):
    form_class = DesignationCreateForm
    template_name = 'officialdata/designation_form.html'
    # success_url = '/designation/list/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DesignationListView(LoginRequiredMixin, ListView):
    model = Designation
    template_name = 'designation/designation_list.html'

class DesignationDetailView(LoginRequiredMixin, DetailView):
    model = Designation
    context_object_name = 'designation'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_designation'] = self.model.objects.all()
        return context

class DesignationUpdateView(LoginRequiredMixin, UpdateView):
    model = Designation
    fields = ['designation_nepali', 'designation_english']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DesignationDeleteView(LoginRequiredMixin, DeleteView):
    model = Designation
    success_url = '/designation/list/'

'''  --------------------------------------------------------------------------------------------------------
					Employee Type Addition Views Starts Here (स्थायी / Permanent, करार / Contract etc. 
-----------------------------------------------------------------------------------------------------------'''

class EmployeeTypeCreateView(LoginRequiredMixin, CreateView):
    form_class = EmployeeTypeCreateForm
    template_name = 'officialdata/employeetype_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EmployeeTypeListView(LoginRequiredMixin, ListView):
    model = Employeetype
    template_name = 'employeetype/employeetype_list.html'

class EmployeeTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employeetype
    fields = ['employeetype_nepali', 'employeetype_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EmployeeTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employeetype
    success_url = '/employeetype/list/'