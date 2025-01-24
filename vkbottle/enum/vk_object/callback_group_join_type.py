from enum import StrEnum


class CallbackGroupJoinType(StrEnum):
    """ CallbackGroupJoinType enum """

    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"
