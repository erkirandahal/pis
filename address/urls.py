from django.urls import path
from . import views
from .views import (
    ProvinceCreateView,
    ProvinceListView,
    LocalLevelTypeCreateView,
    LocalLevelListView,
    AddressListView
)

urlpatterns = [
    path('province/create/', ProvinceCreateView.as_view(), name='province-create'),
    path('province/list/', ProvinceListView.as_view(), name='province-list'),
    path('localleveltype/create/', LocalLevelTypeCreateView.as_view(), name='localleveltype-create'),
    path('localleveltype/list/', LocalLevelListView.as_view(), name='localleveltype-list'),
    path('address/list/', AddressListView.as_view(), name='address-list'),
]
