from django.http import HttpResponse, HttpRequest
from django.http import JsonResponse
from django.shortcuts import render
from currency_server.calculations import *
from currency_server.nbp_api import *
from typing import Union


def index(request: HttpRequest) -> HttpResponse:
    port = request.META.get('SERVER_PORT')
    context = {'port': port}
    return render(request, 'currency_server/index.html', context)


def one_day_rate(request: HttpRequest, currency: str, date: str) -> Union[JsonResponse, HttpResponse]:
    response = average_exchange_rate_request(currency, date)
    if response.status_code != 200:
        return HttpResponse(status=response.status_code)
    avg_rate = average_exchange_rate(response.json())
    response_data = {'avg_rate': avg_rate}
    return JsonResponse(response_data)


def maximum_and_minimum_rates(request: HttpRequest, currency: str, number_quotations: int) \
        -> Union[JsonResponse, HttpResponse]:
    try:
        response = max_and_min_of_exchange_rate_request(currency, number_quotations)
    except ValueError:
        return HttpResponse(status=400)
    if response.status_code != 200:
        return HttpResponse(status=response.status_code)
    maximum_average_exchange, minimum_average_exchange = max_and_min_of_exchange_rate(response.json())
    response_data = {'maximum': maximum_average_exchange, 'minimum': minimum_average_exchange}
    return JsonResponse(response_data)


def buy_and_sell_rates(request: HttpRequest, currency: str, number_quotations: int) \
        -> Union[JsonResponse, HttpResponse]:
    try:
        response = max_diff_buy_ask_rate_request(currency, number_quotations)
    except ValueError:
        return HttpResponse(status=400)
    if response.status_code != 200:
        return HttpResponse(status=response.status_code)
    abs_max_difference = max_diff_buy_ask_rate(response.json())
    response_data = {'abs_max_difference': abs_max_difference}
    return JsonResponse(response_data)
