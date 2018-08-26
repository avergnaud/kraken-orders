"""
Cf https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
Factories allow more flexible object creation
"""
from kraken.orders.Orders import Orders
from kraken.orders.impl.LimitOrder import LimitOrder
from kraken.orders.impl.MarketOrder import MarketOrder


class KrakenOrderFactory:

    def get_order(self, type):
        if type == Orders.Limit:
            return LimitOrder()
        if type == Orders.Market:
            return MarketOrder()
