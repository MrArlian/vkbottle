from enum import IntEnum


class BoardDefaultOrder(IntEnum):
    """ Sort type """

    desc_updated = 1
    desc_created = 2
    asc_updated = -1
    asc_created = -2
