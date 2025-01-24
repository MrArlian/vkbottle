from __future__ import annotations

from typing import Optional

from ...base import VkObject


class MemberStatusFull(VkObject):
    """VK Object GroupsMemberStatusFull

    can_invite - Information whether user can be invited
    can_recall - Information whether user's invite to the group can be recalled
    invitation - Information whether user has been invited to the group
    member - Information whether user is a member of the group
    request - Information whether user has send request to the group
    user_id - User ID
    """

    can_invite: Optional[bool] = None
    can_recall: Optional[bool] = None
    invitation: Optional[bool] = None
    member: bool
    request: Optional[bool] = None
    user_id: int
