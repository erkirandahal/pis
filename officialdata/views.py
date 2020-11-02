from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import DesignationCreateForm
from .models import Designation
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