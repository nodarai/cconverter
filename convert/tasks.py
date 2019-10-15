import requests
from django.conf import settings
from celery import task 
from celery import shared_task 

from convert.models import Currency, CurrencyRate


@shared_task
def update_rates():
    url = 'https://openexchangerates.org/api/latest.json?base={}&app_id={}'
    currencies = Currency.objects.all()
    currency_rates = []
    for currency_base in currencies:
        results = requests.get(url.format(currency_base.code,settings.OPENEXCHANGE_APIKEY))
        if results.status_code == 200:
            rates = results.json()['rates']
            for currency in currencies:
                if currency_base.code != currency.code:
                    currency_rates.append(
                        CurrencyRate(
                            convert_from=currency_base,
                            convert_to=currency,
                            rate=rates.get(currency.code, -1)
                        )
                    )
    CurrencyRate.objects.bulk_create(currency_rates)
