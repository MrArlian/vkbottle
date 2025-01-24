from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Replies(VkObject):
    """VK Object StoriesReplies

    count - Replies number.
    new - New replies number.
    """

    count: int
    new: Optional[int] = None
