import pytest
from currency_server.calculations import *


@pytest.mark.parametrize("response_json, expected_average", [
    ({'table': 'A', 'currency': 'some currency', 'code': 'code',
      'rates': [{'no': '001/A/NBP/2023', 'effectiveDate': '2023-01-01', 'mid': 4.5677}]}, 4.5677),
    ({'table': 'A', 'currency': 'some currency', 'code': 'code',
      'rates': [{'no': '002/A/NBP/2023', 'effectiveDate': '2023-01-02', 'mid': 3.4231}]}, 3.4231),
    ({'table': 'A', 'currency': 'some currency', 'code': 'code',
      'rates': [{'no': '003/A/NBP/2023', 'effectiveDate': '2023-01-03', 'mid': 1.9005}]}, 1.9005),
    ({'table': 'A', 'currency': 'funt szterling', 'code': 'GBP',
      'rates': [{'no': '078/A/NBP/2023', 'effectiveDate': '2023-04-21', 'mid': 5.2086}]}, 5.2086)
])
def test_average_exchange_rate(response_json, expected_average):
    assert average_exchange_rate(response_json) == expected_average


@pytest.mark.parametrize("response_json, expected_average", [
    ({
         'table': 'A',
         'currency': 'funt szterling',
         'code': 'GBP',
         'rates': [{'no': '057/A/NBP/2023', 'effectiveDate': '2023-03-22', 'mid': 5.3385},
                   {'no': '058/A/NBP/2023', 'effectiveDate': '2023-03-23', 'mid': 5.2966},
                   {'no': '059/A/NBP/2023', 'effectiveDate': '2023-03-24', 'mid': 5.3417},
                   {'no': '060/A/NBP/2023', 'effectiveDate': '2023-03-27', 'mid': 5.3364}
                   ]
     }, (5.3417, 5.2966)),
    ({
         'table': 'A',
         'currency': 'funt szterling',
         'code': 'GBP',
         'rates': [{'no': '057/A/NBP/2023', 'effectiveDate': '2023-03-22', 'mid': 5.0000},
                   {'no': '058/A/NBP/2023', 'effectiveDate': '2023-03-23', 'mid': 3.0000},
                   {'no': '059/A/NBP/2023', 'effectiveDate': '2023-03-24', 'mid': 4.0000},
                   {'no': '060/A/NBP/2023', 'effectiveDate': '2023-03-27', 'mid': 7.0000},
                   {'no': '061/A/NBP/2023', 'effectiveDate': '2023-03-28', 'mid': 1.0000},
                   {'no': '062/A/NBP/2023', 'effectiveDate': '2023-03-29', 'mid': 0.1000},
                   {'no': '063/A/NBP/2023', 'effectiveDate': '2023-03-30', 'mid': 2.0000}
                   ]
     }, (7.0000, 0.1000)),
    ({
         'table': 'A',
         'currency': 'funt szterling',
         'code': 'GBP',
         'rates': [{'no': '057/A/NBP/2023', 'effectiveDate': '2023-03-22', 'mid': 5.0000}]
     }, (5.0000, 5.0000)),
    ({
         'table': 'A',
         'currency': 'funt szterling',
         'code': 'GBP',
         'rates': [{'no': '057/A/NBP/2023', 'effectiveDate': '2023-03-22', 'mid': 4.5005},
                   {'no': '057/A/NBP/2023', 'effectiveDate': '2023-03-23', 'mid': 5.5005}
                   ]
     }, (5.5005, 4.5005)),
])
def test_max_and_min_of_exchange_rate(response_json, expected_average):
    assert max_and_min_of_exchange_rate(response_json) == expected_average


@pytest.mark.parametrize("response_json, expected_average", [
    ({'table': 'C',
      'currency': 'funt szterling',
      'code': 'GBP',
      'rates': [{'no': '076/C/NBP/2023', 'effectiveDate': '2023-04-19', 'bid': 4.7000, 'ask': 5.0000},
                {'no': '077/C/NBP/2023', 'effectiveDate': '2023-04-20', 'bid': 5.1000, 'ask': 5.6000},
                {'no': '078/C/NBP/2023', 'effectiveDate': '2023-04-21', 'bid': 5.0000, 'ask': 6.0000},
                {'no': '079/C/NBP/2023', 'effectiveDate': '2023-04-24', 'bid': 5.2000, 'ask': 5.6000}]
      }, 1.0000),
    ({'table': 'C',
      'currency': 'funt szterling',
      'code': 'GBP',
      'rates': [{'no': '076/C/NBP/2023', 'effectiveDate': '2023-04-19', 'bid': 4.7000, 'ask': 5.1000}]
      }, 0.4000),
    ({'table': 'C',
      'currency': 'funt szterling',
      'code': 'GBP',
      'rates': [{'no': '076/C/NBP/2023', 'effectiveDate': '2023-04-19', 'bid': 4.7000, 'ask': 5.0000},
                {'no': '077/C/NBP/2023', 'effectiveDate': '2023-04-20', 'bid': 5.1000, 'ask': 5.4000},
                {'no': '078/C/NBP/2023', 'effectiveDate': '2023-04-21', 'bid': 5.0000, 'ask': 5.2000},
                {'no': '079/C/NBP/2023', 'effectiveDate': '2023-04-24', 'bid': 5.2000, 'ask': 5.3000}]
      }, 0.3000),
])
def test_max_diff_buy_ask_rate(response_json, expected_average):
    assert max_diff_buy_ask_rate(response_json) == expected_average
