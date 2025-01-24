from __future__ import annotations

from ...base import VkObject


class FriendsList(VkObject):
    """VK Object FriendsFriendsList

    id - List ID
    name - List title
    """

    id: int
    name: str
