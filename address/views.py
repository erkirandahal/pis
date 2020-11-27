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
from officedata.views import UserAccessMixin

class ProvinceCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'address.add_province'
    form_class = ProvinceCreateForm
    template_name = 'address/province_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProvinceListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'address.list_province'
    model = Province
    template_name = 'province/province_list.html'

class ProvinceUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = 'address.change_province'
    model = Province
    fields = ['provincename_nepali', 'provincename_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ProvinceDeleteView(LoginRequiredMixin, DeleteView):
    # pass
    # permission_required = 'address.delete_localleveltype'
    model = Province
    success_url = '/province/list/'

class LocalLevelTypeCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    permission_required = 'address.add_localleveltype'
    form_class = LocalLevelTypeCreateForm
    template_name = 'address/localleveltype_form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class LocalLevelListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'address.list_localleveltype'
    model = LocalLevelType
    template_name = 'address/localleveltype_list.html'


class LocallevelTypeDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'address.delete_localleveltype'
    model = LocalLevelType
    success_url = '/localleveltype/list/'


#GET MORE THAN ONE VIEW TO RENDER IN SINGLE PAGE,

class AddressListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = ('address.list_province', 'address.list_localeveltype')
    template_name = 'address/address_list.html'
    queryset = Province.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AddressListView, self).get_context_data(**kwargs)
        context['localleveltype_list'] = LocalLevelType.objects.all()
        context['province'] = self.queryset
        return context
