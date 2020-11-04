from django.urls import path
from .views import (
    OfficeTypeCreateView,
    OfficeTypeListView,
    OfficeTypeUpdateView,
    OfficeTypeDeleteView,
    OfficeCreateView,
    OfficeListView,
    OfficeUpdateView,
    OfficeDeleteView,
    AllOfficedataView,
)
from . import views

urlpatterns = [
    path('officetype/create', OfficeTypeCreateView.as_view(), name='officetype-create'),
    path('officetype/list', OfficeTypeListView.as_view(), name='officetype-list'),
    path('officetype/update/<int:pk>', OfficeTypeUpdateView.as_view(), name='officetype-update'),
    path('officetype/delete/<int:pk>', OfficeTypeDeleteView.as_view(), name='officetype-delete'),
    path('office/create', OfficeCreateView.as_view(), name='office-create'),
    path('office/list', OfficeListView.as_view(), name='office-list'),
    path('office/update/<int:pk>', OfficeUpdateView.as_view(), name='office-update'),
    path('office/delete/<int:pk>', OfficeDeleteView.as_view(), name='office-delete'),
    path('allofficedata/list', AllOfficedataView.as_view(), name='allofficedata-list'),
]
