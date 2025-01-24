from enum import StrEnum


class MessagesChatSettingsPermissionsSeeInviteLink(StrEnum):
    """ Who can see invite link """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"
