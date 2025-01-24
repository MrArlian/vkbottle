from enum import IntEnum


class FriendsFriendStatusStatus(IntEnum):
    """ Friend status with the user """

    not_a_friend = 0
    outcoming_request = 1
    incoming_request = 2
    is_friend = 3
