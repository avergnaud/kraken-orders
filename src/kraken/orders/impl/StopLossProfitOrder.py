"""
https://stackoverflow.com/questions/551038/private-implementation-class-in-python
"""
from kraken.orders.KrakenOrder import KrakenOrder


class StopLossProfit(KrakenOrder):

    def __init__(self):
        self._stop_loss_price = None
        self._take_profit_price = None

    def get_stop_loss_price(self):
        return self._stop_loss_price

    def set_stop_loss_price(self, stop_loss_price):
        self._stop_loss_price = stop_loss_price

    def get_take_profit_price(self):
        return self._take_profit_price

    def set_take_profit_price(self, take_profit_price):
        self._take_profit_price = take_profit_price

    def description(self):
        pass

    def execute(self):
        if self._stop_loss_price is None:
            raise ValueError("stop_loss_price is None")
        if self._take_profit_price is None:
            raise ValueError("_take_profit_price is None")
        pass
