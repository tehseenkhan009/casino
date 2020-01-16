from django.urls import path

from .views import (
    CasinoListAPIView, DealsListAPIView
)

urlpatterns = [
    path('', CasinoListAPIView.as_view(), name='casino-list'),
    path('deals', DealsListAPIView.as_view(), name='deals-list'),
    path('take', CasinoListAPIView.as_view(), name='casino-details'),
]
