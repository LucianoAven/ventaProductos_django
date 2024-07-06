import requests
from django.core.cache import cache

from product.models import Product

def dolar_exchange_rates(request):

    exchange_rates = cache.get('exchange_rates')

    if exchange_rates is None:

        exchange_rates = requests.get("https://dolarapi.com/v1/dolares").json()
        cache.set('exchange_rates', exchange_rates, 600)

    return dict(
        valores_dolar=exchange_rates
    )
