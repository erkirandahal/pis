from django.urls import path
from . import views
from .views import (
    ProvinceCreateView,
    ProvinceListView,
    LocalLevelTypeCreateView,
    LocalLevelListView,
    AddressListView,
    ProvinceUpdateView,
    ProvinceDeleteView,
    LocallevelTypeDeleteView,
)

urlpatterns = [
    path('province/create/', ProvinceCreateView.as_view(), name='province-create'),
    path('province/list/', ProvinceListView.as_view(), name='province-list'),
    path('province/update/<int:pk>', ProvinceUpdateView.as_view(), name='province-update'),
    path('province/delete/<int:pk>', ProvinceDeleteView.as_view(), name='province-delete'),
    path('localleveltype/create/', LocalLevelTypeCreateView.as_view(), name='localleveltype-create'),
    path('localleveltype/list/', LocalLevelListView.as_view(), name='localleveltype-list'),
    path('localleveltype/delete/<int:pk>', LocallevelTypeDeleteView.as_view(), name='localleveltype-delete'),
    path('address/list/', AddressListView.as_view(), name='address-list'),
]
