from enum import IntEnum


class MarketMarketItemAvailability(IntEnum):
    """ Information whether the item is available """

    available = 0
    removed = 1
    unavailable = 2
