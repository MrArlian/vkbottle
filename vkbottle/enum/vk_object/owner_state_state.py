from enum import IntEnum


class OwnerStateState(IntEnum):
    """ OwnerStateState enum """

    banned = 1
    adult = 2
    hidden = 3
    deleted = 4
    blacklisted = 5
