from enum import StrEnum


class GroupsRoleOptions(StrEnum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
