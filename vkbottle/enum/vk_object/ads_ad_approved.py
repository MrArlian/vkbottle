from enum import IntEnum


class AdsAdApproved(IntEnum):
    """ Review status """

    not_moderated = 0
    pending_moderation = 1
    approved = 2
    rejected = 3
