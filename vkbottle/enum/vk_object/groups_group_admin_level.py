from enum import IntEnum


class GroupsGroupAdminLevel(IntEnum):
    """ Level of current user's credentials as manager """

    moderator = 1
    editor = 2
    administrator = 3
