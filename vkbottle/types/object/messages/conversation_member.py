from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ConversationMember(VkObject):
    """VK Object MessagesConversationMember

    can_kick - Is it possible for user to kick this member
    invited_by -
    is_admin -
    is_message_request -
    is_owner -
    join_date -
    member_id -
    request_date - Message request date
    """

    can_kick: Optional[bool] = None
    invited_by: Optional[int] = None
    is_admin: Optional[bool] = None
    is_message_request: Optional[bool] = None
    is_owner: Optional[bool] = None
    join_date: Optional[int] = None
    member_id: int
    request_date: Optional[int] = None
