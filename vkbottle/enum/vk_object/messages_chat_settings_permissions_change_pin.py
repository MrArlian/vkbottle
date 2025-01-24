from enum import StrEnum


class MessagesChatSettingsPermissionsChangePin(StrEnum):
    """ Who can change pinned message """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"
