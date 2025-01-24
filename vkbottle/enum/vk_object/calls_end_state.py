from enum import StrEnum


class CallsEndState(StrEnum):
    """ State in which call ended up """

    CANCELED_BY_INITIATOR = "canceled_by_initiator"
    CANCELED_BY_RECEIVER = "canceled_by_receiver"
    REACHED = "reached"
