from enum import IntEnum


class AdsCampaignStatus(IntEnum):
    """ Campaign status """

    stopped = 0
    started = 1
    deleted = 2
