from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import OfficeTypeCreateForm
from .models import Officetype
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
