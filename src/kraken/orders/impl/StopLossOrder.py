"""
https://stackoverflow.com/questions/551038/private-implementation-class-in-python
"""
from kraken.orders.KrakenOrder import KrakenOrder


class StopLossOrder(KrakenOrder):

    def __init__(self):
        self._stop_loss_price = None

    def get_stop_loss_price(self):
        return self._stop_loss_price

    def set_stop_loss_price(self, stop_loss_price):
        self._stop_loss_price = stop_loss_price

    def description(self):
        pass

    def execute(self):
        if self._stop_loss_price is None:
            raise ValueError("stop_loss_price is None")
        pass
