from enum import IntEnum


class GroupsGroupFullWall(IntEnum):
    """ Information about wall status in community """

    disabled = 0
    open = 1
    limited = 2
    restricted = 3
