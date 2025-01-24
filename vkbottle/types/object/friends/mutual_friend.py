from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class MutualFriend(VkObject):
    """VK Object FriendsMutualFriend

    common_count - Total mutual friends number
    common_friends -
    id - User ID
    """

    common_count: Optional[int] = None
    common_friends: Optional[List[int]] = None
    id: Optional[int] = None
