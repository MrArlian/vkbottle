from enum import StrEnum


class MessagesChatSettingsPermissionsChangeInfo(StrEnum):
    """ Who can change chat info """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"
