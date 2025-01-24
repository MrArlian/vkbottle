from __future__ import annotations

from ...base import VkObject


class FeedList(VkObject):
    """VK Object NewsfeedList

    id - List ID
    title - List title
    """

    id: int
    title: str
