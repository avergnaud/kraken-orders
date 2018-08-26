"""
see https://www.orders.com/help/api#private-user-data
seule classe accessible du package kraken.orders,
cf https://stackoverflow.com/questions/551038/private-implementation-class-in-python
"""


class KrakenOrder:

    def __init__(self):
        pass

    '''
    follows the python adage "we're all adults here" - 
    if a subclass doesn't implement this type of abstract method, it will have to deal with the consequences
    '''
    def description(self):
        raise NotImplementedError("Please Implement this method")

    def execute(self):
        pass
