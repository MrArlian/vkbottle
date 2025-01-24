from enum import StrEnum


class GroupsMarketState(StrEnum):
    """ Declares state if market is enabled in group. """

    NONE = "none"
    BASIC = "basic"
    ADVANCED = "advanced"
