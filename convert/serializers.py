from rest_framework import serializers

from convert.models import Currency, CurrencyRate


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('code', 'full_name')


class CurrencyRateSerializer(serializers.ModelSerializer):
    convert_from = serializers.StringRelatedField(many=False)
    convert_to = serializers.StringRelatedField(many=False)

    class Meta:
        model = CurrencyRate
        fields = ('convert_from', 'convert_to', 'rate', 'created_at')
