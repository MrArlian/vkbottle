from enum import StrEnum


class WhoCanChangeAdmins(StrEnum):
    """ Who can change admins """

    OWNER = "owner"
    OWNER_AND_ADMINS = "owner_and_admins"
