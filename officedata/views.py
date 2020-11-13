from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .forms import OfficeTypeCreateForm, OfficeCreateForm
from .models import Officetype, Office
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView,)

class UserAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/')
        return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)


class OfficeTypeCreateView(LoginRequiredMixin, UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'officedata.add_officetype'
    permission_denied_message = ""
    login_url = '/officetype/list/'
    redirect_field_name = 'next'
    form_class = OfficeTypeCreateForm
    # template_name = 'officedata/officetype_form.html'
    template_name = 'officedata/officetype_form.html'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeTypeListView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = 'officedata.view_officetype'
    model = Officetype
    template_name = 'officetype/officetype_list.html'

class OfficeTypeUpdateView(LoginRequiredMixin, UserAccessMixin, UpdateView):
    permission_required = 'officedata.change_officetype'
    model = Officetype
    fields = ['officetype_nepali', 'officetype_english']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeTypeDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'officedata.delete_officetype'
    model = Officetype
    success_url = '/officetype/list'

class OfficeCreateView(UserAccessMixin, CreateView):
    raise_exception = False
    permission_required = 'officedata.add_office'
    permission_denied_message = ""
    # login_url = '/office/list/'
    # redirect_field_name = 'next'

    form_class = OfficeCreateForm
    template_name = 'officedata/office_form.html'


    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeListView(LoginRequiredMixin, UserAccessMixin, ListView):
    # raise_exception = False
    permission_required = 'officedata.view_office'
    # permission_denied_message = ""
    # login_url = '/office/list/'
    # redirect_field_name = 'next'

    model = Office
    template_name = 'officetype/office_list.html'


class OfficeUpdateView(UserAccessMixin, UpdateView):
    raise_exception = False
    permission_required = 'officedata.change_office'
    permission_denied_message = ""
    login_url = '/office/list/'
    redirect_field_name = 'next'

    model = Office
    fields = ['officename_nepali', 'officename_english', 'officeaddress', 'officetype', 'office_wardno']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class OfficeDeleteView(LoginRequiredMixin, UserAccessMixin, DeleteView):
    permission_required = 'officedata.delete_office'
    model = Office
    success_url = '/office/list'


#GET MORE THAN ONE VIEW TO RENDER IN SINGLE PAGE,

class AllOfficedataView(LoginRequiredMixin, UserAccessMixin, ListView):
    permission_required = ('officedata.view_office', 'officedata.view_officetype')
    template_name = 'officedata/allofficedata_list.html'
    queryset = Officetype.objects.all()

    def get_context_data(self, **kwargs):
        context = super(AllOfficedataView, self).get_context_data(**kwargs)
        context['office_list'] = Office.objects.all()
        context['officetype_list'] = self.queryset
        return context