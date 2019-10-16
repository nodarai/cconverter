from rest_framework import viewsets, generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from convert.models import Currency, CurrencyRate
from convert.serializers import CurrencySerializer, CurrencyRateSerializer


class CurrencyViewSet(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyRatesViewSet(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CurrencyRate.objects.all()
    serializer_class = CurrencyRateSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['convert_from__code', 'convert_to__code']

