import pytest
from currency_server.nbp_api import *
from unittest import mock
from requests import Response


def test_average_exchange_rate_request_success():
    currency = 'USD'
    date = '2023-04-24'
    expected_url = f'https://api.nbp.pl/api/exchangerates/rates/A/{currency}/{date}/'
    expected_response = Response()
    expected_response.status_code = 200

    with mock.patch('requests.get', return_value=expected_response) as mock_get:
        response = average_exchange_rate_request(currency, date)

    assert response == expected_response
    mock_get.assert_called_once_with(expected_url)


def test_max_and_min_of_exchange_rate_request_success():
    currency = 'USD'
    number_quotations = 3
    expected_url = f'https://api.nbp.pl/api/exchangerates/rates/A/{currency}/last/{number_quotations}/'
    expected_response = Response()
    expected_response.status_code = 200
    with mock.patch('requests.get', return_value=expected_response) as mock_get:
        response = max_and_min_of_exchange_rate_request(currency, number_quotations)

    assert response == expected_response
    mock_get.assert_called_once_with(expected_url)


@pytest.mark.parametrize('number_quotations', [0, 256, 1000])
def test_max_and_min_of_exchange_rate_request_with_invalid_param(number_quotations):
    currency = 'USD'
    with pytest.raises(ValueError):
        max_and_min_of_exchange_rate_request(currency, number_quotations)


def test_max_diff_buy_ask_rate_request_success():
    currency = 'USD'
    number_quotations = 3
    expected_url = f'https://api.nbp.pl/api/exchangerates/rates/C/{currency}/last/{number_quotations}/'
    expected_response = Response()
    expected_response.status_code = 200
    with mock.patch('requests.get', return_value=expected_response) as mock_get:
        response = max_diff_buy_ask_rate_request(currency, number_quotations)

    assert response == expected_response
    mock_get.assert_called_once_with(expected_url)


@pytest.mark.parametrize('number_quotations', [0, 256, 1000])
def test_max_diff_buy_ask_rate_request_with_invalid_param(number_quotations):
    currency = 'USD'
    with pytest.raises(ValueError):
        max_diff_buy_ask_rate_request(currency, number_quotations)
