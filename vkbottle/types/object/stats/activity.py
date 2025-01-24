from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Activity(VkObject):
    """VK Object StatsActivity

    comments - Comments number
    copies - Reposts number
    hidden - Hidden from news count
    likes - Likes number
    subscribed - New subscribers count
    unsubscribed - Unsubscribed count
    """

    comments: Optional[int] = None
    copies: Optional[int] = None
    hidden: Optional[int] = None
    likes: Optional[int] = None
    subscribed: Optional[int] = None
    unsubscribed: Optional[int] = None
