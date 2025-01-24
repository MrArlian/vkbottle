from enum import StrEnum


class AdsAccessRolePublic(StrEnum):
    """ Current user's role """

    MANAGER = "manager"
    REPORTS = "reports"
