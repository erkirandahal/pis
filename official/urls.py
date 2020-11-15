from django.urls import path
from .views import (
    StaffCreateView,
    StaffListView,
    StaffUpdateView,
    StaffDetailView,
    UserPostListView,

)
from . import views

urlpatterns = [
    path('staff/create/', StaffCreateView.as_view(), name='staff-create'),
    path('staff/list/', StaffListView.as_view(), name='staff-list'),
    path('staff/<int:pk>/', StaffDetailView.as_view(), name='staff-detail'),
    path('staff/update/<int:pk>', StaffUpdateView.as_view(), name='staff-update'),
    path('staff/<str:username>', UserPostListView.as_view(), name='staff-post'),
    # path('print/<int: pk>/', OnlickPrint.downloadexcel,name="print-staff"),
    # path('ajax/load-officename/', views.load_officename, name='ajax-load-office')
]