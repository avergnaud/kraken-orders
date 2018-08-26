from kraken.orders.Orders import Orders
from kraken.orders.KrakenOrderFactory import KrakenOrderFactory


factory = KrakenOrderFactory()
order = factory.get_order(Orders.Limit)
order.description()
