from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import OfficeTypeCreateForm, OfficeCreateForm
from .models import Officetype, Office
from django.contrib.auth.models import User
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,)

class OfficeTypeCreateView(LoginRequiredMixin, CreateView):
    form_class = OfficeTypeCreateForm
    # template_name = 'officedata/officetype_form.html'
    template_name = 'officedata/officetype_form.html'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeTypeListView(LoginRequiredMixin, ListView):
    model = Officetype
    template_name = 'officetype/officetype_list.html'

class OfficeTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = Officetype
    fields = ['officetype_nepali', 'officetype_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = Officetype
    success_url = '/officetype/list/'

class OfficeCreateView(LoginRequiredMixin, CreateView):
    form_class = OfficeCreateForm
    template_name = 'officedata/office_form.html'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeListView(LoginRequiredMixin, ListView):
    model = Office
    template_name = 'officetype/office_list.html'


class OfficeUpdateView(LoginRequiredMixin, UpdateView):
    model = Office
    fields = ['officename_nepali', 'officename_english', 'officeaddress', 'officetype']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeDeleteView(LoginRequiredMixin, DeleteView):
    model = Office
    success_url = '/office/list/'


#GET MORE THAN ONE VIEW TO RENDER IN SINGLE PAGE,

class AllOfficedataView(LoginRequiredMixin, ListView):
    template_name = 'officedata/allofficedata_list.html'
    queryset = Officetype.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AllOfficedataView, self).get_context_data(**kwargs)
        context['office_list'] = Office.objects.all()
        context['officetype_list'] = self.queryset
        return context