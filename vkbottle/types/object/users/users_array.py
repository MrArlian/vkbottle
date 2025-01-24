from __future__ import annotations

from typing import List

from ...base import VkObject


class UsersArray(VkObject):
    """VK Object UsersUsersArray

    count - Users number
    items -
    """

    count: int
    items: List[int]
