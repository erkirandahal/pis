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
