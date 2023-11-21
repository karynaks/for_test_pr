from typing import Dict


def average_exchange_rate(response_json: Dict) -> float:
    return response_json['rates'][0]['mid']


def max_and_min_of_exchange_rate(resp_json: Dict) -> (float, float):
    mid_rates = list(map(lambda x: x['mid'], resp_json['rates']))
    return max(mid_rates), min(mid_rates)


def max_diff_buy_ask_rate(resp_json: Dict) -> float:
    diff_buy_ask_rates = map(lambda x: round(x['ask'] - x['bid'], 10), resp_json['rates'])
    return max(diff_buy_ask_rates)
