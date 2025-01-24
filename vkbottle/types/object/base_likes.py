from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseLikes(VkObject):
    """VK Object BaseLikes

    count - Likes number
    user_likes - Information whether current user likes the photo
    """

    count: Optional[int] = None
    user_likes: Optional[bool] = None
