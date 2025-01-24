from enum import IntEnum


class GroupsGroupIsClosed(IntEnum):
    """ Information whether community is closed """

    open = 0
    closed = 1
    private = 2
