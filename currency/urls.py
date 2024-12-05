from django.urls import path
from .views import CurrencyListView, ExchangeRateDetailView

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency-list'),
    path('currency/<str:base_currency>/<str:quote_currency>/', ExchangeRateDetailView.as_view(), name='exchange-rate'),
]
