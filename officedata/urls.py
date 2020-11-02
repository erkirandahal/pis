from django.urls import path
from .views import (OfficeTypeCreateView,
                    OfficeTypeListView,
                    OfficeTypeUpdateView,
                    OfficeTypeDeleteView,
                    )
from . import views

urlpatterns = [
    path('officetype/create', OfficeTypeCreateView.as_view(), name='officetype-create'),
    path('officetype/list/', OfficeTypeListView.as_view(), name='officetype-list'),
    path('officetype/update/<int:pk>', OfficeTypeUpdateView.as_view(), name='officetype-update'),
    path('officetype/delete/<int:pk>', OfficeTypeDeleteView.as_view(), name='officetype-delete'),
]
