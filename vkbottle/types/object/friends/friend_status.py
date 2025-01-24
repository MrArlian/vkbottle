from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import FriendsFriendStatusStatus

from ...base import VkObject


class FriendStatus(VkObject):
    """VK Object FriendsFriendStatus

    friend_status -
    sign - MD5 hash for the result validation
    user_id - User ID
    """

    friend_status: FriendsFriendStatusStatus
    sign: Optional[str] = None
    user_id: int
