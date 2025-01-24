from enum import StrEnum


class GroupsAddressWorkInfoStatus(StrEnum):
    """ Status of information about timetable """

    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"
