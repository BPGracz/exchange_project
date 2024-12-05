from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Currency, ExchangeRate
from .serializers import CurrencySerializer, ExchangeRateSerializer

class CurrencyListView(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

class ExchangeRateDetailView(APIView):
    def get(self, request, base_currency, quote_currency):
        pair = f"{base_currency}{quote_currency}"
        try:
            rate = ExchangeRate.objects.get(currency_pair=pair)
            serializer = ExchangeRateSerializer(rate)
            return Response(serializer.data)
        except ExchangeRate.DoesNotExist:
            return Response({"error": "Exchange rate not found."}, status=404)
