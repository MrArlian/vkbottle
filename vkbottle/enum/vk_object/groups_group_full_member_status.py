from enum import IntEnum


class GroupsGroupFullMemberStatus(IntEnum):
    """ GroupsGroupFullMemberStatus enum """

    not_a_member = 0
    member = 1
    not_sure = 2
    declined = 3
    has_sent_a_request = 4
    invited = 5
