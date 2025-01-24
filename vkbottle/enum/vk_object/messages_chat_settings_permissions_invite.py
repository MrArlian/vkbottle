from enum import StrEnum


class MessagesChatSettingsPermissionsInvite(StrEnum):
    """ Who can invite users to chat """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"
