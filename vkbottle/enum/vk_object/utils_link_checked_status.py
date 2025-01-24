from enum import StrEnum


class UtilsLinkCheckedStatus(StrEnum):
    """ Link status """

    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"
