import json
from currency_server.views import *
from django.test import RequestFactory, TestCase
from django.http import JsonResponse, HttpResponse
from unittest.mock import patch
from requests.models import Response
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'currency_server.settings'


class TestOneDayRate(TestCase):

    def test_one_day_rate(self):
        date = '2023-04-21'
        currency = 'USD'
        expected_rate = 3.50
        mock_response_data = {'table': 'A',
                              'currency': 'currency',
                              'code': currency,
                              'rates': [{'no': '077/A/NBP/2023', 'effectiveDate': date, 'mid': expected_rate}]}
        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps(mock_response_data).encode('utf-8')
        factory = RequestFactory()
        request = factory.get(f'/exchanges/one-day-rate/{currency}/{date}/')

        with patch('currency_server.views.average_exchange_rate_request') as mock_exchange_rate_request:
            mock_exchange_rate_request.return_value = mock_response
            response = one_day_rate(request, currency, date)
            assert isinstance(response, JsonResponse)
            assert response.status_code == 200

        with patch('currency_server.views.average_exchange_rate_request') as mock_exchange_rate_request:
            mock_exchange_rate_request.return_value.status_code = 404
            response = one_day_rate(request, currency, date)
            assert isinstance(response, HttpResponse)
            assert response.status_code == 404


class TestMaximumAndMinimumRates(TestCase):

    def test_maximum_and_minimum_rates(self):
        currency = 'USD'
        number_quotations = 4
        mock_response_data = {
            'table': 'A',
            'currency': 'funt szterling',
            'code': 'GBP',
            'rates': [{'no': '057/A/NBP/2023', 'effectiveDate': '2023-03-22', 'mid': 5.3385},
                      {'no': '058/A/NBP/2023', 'effectiveDate': '2023-03-23', 'mid': 5.2966},
                      {'no': '059/A/NBP/2023', 'effectiveDate': '2023-03-24', 'mid': 5.3417},
                      {'no': '060/A/NBP/2023', 'effectiveDate': '2023-03-27', 'mid': 5.3364}
                      ]
        }

        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps(mock_response_data).encode('utf-8')
        factory = RequestFactory()
        request = factory.get(f'/exchanges/maximum-and-minimum/{currency}/{number_quotations}/')

        with patch('currency_server.views.max_and_min_of_exchange_rate_request') \
                as mock_max_and_min_of_exchange_rate_request:
            mock_max_and_min_of_exchange_rate_request.return_value = mock_response
            response = maximum_and_minimum_rates(request, currency, number_quotations)
            assert isinstance(response, JsonResponse)
            assert response.status_code == 200

        with patch('currency_server.views.max_and_min_of_exchange_rate_request') \
                as mock_max_and_min_of_exchange_rate_request:
            mock_max_and_min_of_exchange_rate_request.return_value.status_code = 404
            response = maximum_and_minimum_rates(request, currency, number_quotations)
            assert isinstance(response, HttpResponse)
            assert response.status_code == 404

        with patch(
                'currency_server.views.max_and_min_of_exchange_rate_request') \
                as mock_max_and_min_of_exchange_rate_request:
            mock_max_and_min_of_exchange_rate_request.side_effect = ValueError
            response = maximum_and_minimum_rates(request, currency, number_quotations)
            assert isinstance(response, HttpResponse)
            assert response.status_code == 400


class TestBuyAndSellRates(TestCase):

    def test_buy_and_sell_rates(self):
        currency = 'USD'
        number_quotations = 4
        mock_response_data = {
            'table': 'C',
            'currency': 'dolar amerykański',
            'code': 'USD',
            'rates': [{'no': '076/C/NBP/2023', 'effectiveDate': '2023-04-19', 'bid': 4.1769, 'ask': 4.2613},
                      {'no': '077/C/NBP/2023', 'effectiveDate': '2023-04-20', 'bid': 4.1677, 'ask': 4.2519},
                      {'no': '078/C/NBP/2023', 'effectiveDate': '2023-04-21', 'bid': 4.1532, 'ask': 4.2372},
                      {'no': '079/C/NBP/2023', 'effectiveDate': '2023-04-24', 'bid': 4.1629, 'ask': 4.2471}]}

        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = json.dumps(mock_response_data).encode('utf-8')
        factory = RequestFactory()
        request = factory.get(f'/buy-and-sell-rates /{currency}/{number_quotations}/')

        with patch('currency_server.views.max_diff_buy_ask_rate_request') \
                as mock_max_diff_buy_ask_rate_request:
            mock_max_diff_buy_ask_rate_request.return_value = mock_response
            response = buy_and_sell_rates(request, currency, number_quotations)
            assert isinstance(response, JsonResponse)
            assert response.status_code == 200

        with patch('currency_server.views.max_diff_buy_ask_rate_request') \
                as mock_max_diff_buy_ask_rate_request:
            mock_max_diff_buy_ask_rate_request.return_value.status_code = 404
            response = buy_and_sell_rates(request, currency, number_quotations)
            assert isinstance(response, HttpResponse)
            assert response.status_code == 404

        with patch('currency_server.views.max_diff_buy_ask_rate_request') \
                as mock_max_diff_buy_ask_rate_request:
            mock_max_diff_buy_ask_rate_request.side_effect = ValueError
            response = buy_and_sell_rates(request, currency, number_quotations)
            assert isinstance(response, HttpResponse)
            assert response.status_code == 400
