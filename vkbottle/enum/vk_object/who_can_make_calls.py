from enum import StrEnum


class WhoCanMakeCalls(StrEnum):
    """ Who can make calls """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
    ALL = "all"
