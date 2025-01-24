from enum import IntEnum


class GroupsBanInfoReason(IntEnum):
    """ Ban reason """

    other = 0
    spam = 1
    verbal_abuse = 2
    strong_language = 3
    flood = 4
