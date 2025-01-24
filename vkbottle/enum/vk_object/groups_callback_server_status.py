from enum import StrEnum


class GroupsCallbackServerStatus(StrEnum):
    """ GroupsCallbackServerStatus enum """

    UNCONFIGURED = "unconfigured"
    FAILED = "failed"
    WAIT = "wait"
    OK = "ok"
