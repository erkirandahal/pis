from django.urls import path
from .views import (
    StaffCreateView,
    StaffListView
)
from . import views

urlpatterns = [
    path('staff/create/', StaffCreateView.as_view(), name='staff-create'),
    path('staff/list/', StaffListView.as_view(), name='staff-list'),
    # path('ajax/load-officename/', views.load_officename, name='ajax-load-office')
]