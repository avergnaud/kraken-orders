"""
https://stackoverflow.com/questions/551038/private-implementation-class-in-python
"""
from kraken.orders.KrakenOrder import KrakenOrder


class MarketOrder(KrakenOrder):

    def description(self):
        pass
