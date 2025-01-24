from enum import StrEnum


class AdsAccessRole(StrEnum):
    """ Current user's role """

    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"
