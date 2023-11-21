import requests as req
from requests.models import Response


def average_exchange_rate_request(currency: str, date: str) -> Response:
    return req.get(f'https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/')


def max_and_min_of_exchange_rate_request(currency: str, number_quotations: int) -> Response:
    if number_quotations < 1 or number_quotations > 255:
        raise ValueError('Invalid number of quotations')
    return req.get(f'https://api.nbp.pl/api/exchangerates/rates/A/{currency}/last/{number_quotations}/')


def max_diff_buy_ask_rate_request(currency: str, number_quotations: int) -> Response:
    if number_quotations < 1 or number_quotations > 255:
        raise ValueError('Invalid number of quotations')
    return req.get(f'https://api.nbp.pl/api/exchangerates/rates/C/{currency}/last/{number_quotations}/')
