from enum import StrEnum


class MessagesChatSettingsPermissionsUseMassMentions(StrEnum):
    """ Who can use mass mentions """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"
