from enum import IntEnum


class AdsAdCostType(IntEnum):
    """ Cost type """

    per_clicks = 0
    per_impressions = 1
    per_actions = 2
    per_impressions_optimized = 3
