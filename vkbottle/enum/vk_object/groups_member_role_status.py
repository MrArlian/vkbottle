from enum import StrEnum


class GroupsMemberRoleStatus(StrEnum):
    """ User's credentials as community admin """

    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"
    ADVERTISER = "advertiser"
