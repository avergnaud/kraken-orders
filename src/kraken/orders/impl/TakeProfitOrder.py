"""
https://stackoverflow.com/questions/551038/private-implementation-class-in-python
"""
from kraken.orders.KrakenOrder import KrakenOrder


class TakeProfitOrder(KrakenOrder):

    def __init__(self):
        self._take_profit_price = None

    def get_take_profit_price(self):
        return self._take_profit_price

    def set_take_profit_price(self, take_profit_price):
        self._take_profit_price = take_profit_price

    def description(self):
        pass

    def execute(self):
        if self._take_profit_price is None:
            raise ValueError("take_profit_price is None")
        pass
