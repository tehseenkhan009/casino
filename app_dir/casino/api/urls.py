from django.urls import path

from .views import (
    CasinoListAPIView, DealsListAPIView, DealActions
)

urlpatterns = [
    path('', CasinoListAPIView.as_view(), name='casino-list'),
    path('deals', DealsListAPIView.as_view(), name='deals-list'),
    path('deals/clicked', DealActions.as_view(), name='deal-clicked'),
    path('take', CasinoListAPIView.as_view(), name='casino-details'),
]
