from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseLinkRating(VkObject):
    """VK Object BaseLinkRating

    reviews_count - Count of reviews
    stars - Count of stars
    """

    reviews_count: Optional[int] = None
    stars: Optional[float] = None
