from __future__ import annotations

from ...base import VkObject


class MemberStatus(VkObject):
    """VK Object GroupsMemberStatus

    member - Information whether user is a member of the group
    user_id - User ID
    """

    member: bool
    user_id: int
