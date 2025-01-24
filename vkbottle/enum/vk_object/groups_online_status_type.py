from enum import StrEnum


class GroupsOnlineStatusType(StrEnum):
    """ Type of online status of group """

    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"
