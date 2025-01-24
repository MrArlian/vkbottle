from enum import StrEnum


class BaseLinkProductStatus(StrEnum):
    """ Status representation """

    ACTIVE = "active"
    BLOCKED = "blocked"
    SOLD = "sold"
    DELETED = "deleted"
    ARCHIVED = "archived"
