"""
https://stackoverflow.com/questions/551038/private-implementation-class-in-python
"""
from kraken.orders.KrakenOrder import KrakenOrder


class LimitOrder(KrakenOrder):

    def __init__(self):
        self._limit_price = None

    def get_limit_price(self):
        return self._limit_price

    def set_limit_price(self, limit_price):
        self._limit_price = limit_price

    def description(self):
        print('description: LimitOrder')

    def execute(self):
        if self._limit_price is None:
            raise ValueError("limit_price is None")
        pass

