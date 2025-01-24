from enum import StrEnum


class LiveStreamStatus(StrEnum):
    """ Live stream status """

    WAITING = "waiting"
    STARTED = "started"
    FINISHED = "finished"
    FAILED = "failed"
    UPCOMING = "upcoming"
