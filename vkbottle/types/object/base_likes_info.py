from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseLikesInfo(VkObject):
    """VK Object BaseLikesInfo

    can_like - Information whether current user can like the post
    can_publish - Information whether current user can repost
    count - Likes number
    user_likes - Information whether current uer has liked the post
    """

    can_like: bool
    can_publish: Optional[bool] = None
    count: int
    user_likes: int
