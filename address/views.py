from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProvinceCreateForm, LocalLevelTypeCreateForm
from .models import Province, LocalLevelType
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)

class ProvinceCreateView(LoginRequiredMixin, CreateView):
    form_class = ProvinceCreateForm
    template_name = 'address/province_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProvinceListView(LoginRequiredMixin, ListView):
    model = Province
    template_name = 'province/province_list.html'

class LocalLevelTypeCreateView(LoginRequiredMixin, CreateView):
    form_class = LocalLevelTypeCreateForm
    template_name = 'address/localleveltype_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LocalLevelListView(LoginRequiredMixin, ListView):
    model = LocalLevelType
    template_name = 'address/localleveltype_list.html'

#GET MORE THAN ONE VIEW TO RENDER IN SINGLE PAGE,

class AddressListView(LoginRequiredMixin, ListView):
    template_name = 'address/address_list.html'
    queryset = Province.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AddressListView, self).get_context_data(**kwargs)
        context['local'] = LocalLevelType.objects.all()
        context['province'] = self.queryset
        return context
