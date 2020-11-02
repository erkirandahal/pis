from django.urls import path
from .views import (
    DesignationCreateView,
    DesignationListView,
    DesignationDetailView,
    DesignationUpdateView,
    DesignationDeleteView,
    EmployeeTypeCreateView,
    EmployeeTypeListView,
    EmployeeTypeUpdateView,
    EmployeeTypeDeleteView,
    SectionTypeCreateView,
    SectionTypeListView,
)
from . import views

urlpatterns = [
    path('designation/create/', DesignationCreateView.as_view(), name='designation-create'),
    path('designation/list/', DesignationListView.as_view(), name='designation-list'),
    path('designation/list/<int:pk>', DesignationDetailView.as_view(), name='designation-detail'),
    path('designation/update/<int:pk>', DesignationUpdateView.as_view(), name='designation-update'),
    path('designation/delete/<int:pk>', DesignationDeleteView.as_view(), name='designation-delete'),
    path('employeetype/create/', EmployeeTypeCreateView.as_view(), name='employeetype-create'),
    path('employeetype/list/', EmployeeTypeListView.as_view(), name='employeetype-list'),
    path('employeetype/update/<int:pk>', EmployeeTypeUpdateView.as_view(), name='employeetype-update'),
    path('employeetype/delete/<int:pk>', EmployeeTypeDeleteView.as_view(), name='employeetype-delete'),
    path('sectiontype/create/', SectionTypeCreateView.as_view(), name='sectiontype-create'),
    path('sectiontype/list/', SectionTypeListView.as_view(), name='sectiontype-list'),
]
