from django.urls import path
from .views import (
    DesignationCreateView,
    DesignationListView,
    DesignationDetailView,
    DesignationUpdateView,
    DesignationDeleteView
)
from . import views

urlpatterns = [
    path('designation/create/', DesignationCreateView.as_view(), name='designation-create'),
    path('designation/list/', DesignationListView.as_view(), name='designation-list'),
    path('designation/list/<int:pk>', DesignationDetailView.as_view(), name='designation-detail'),
    path('designation/update/<int:pk>', DesignationUpdateView.as_view(), name='designation-update'),
    path('designation/delete/<int:pk>', DesignationDeleteView.as_view(), name='designation-delete'),
]
