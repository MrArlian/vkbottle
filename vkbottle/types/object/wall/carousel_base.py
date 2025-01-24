from __future__ import annotations

from typing import Optional

from ...base import VkObject


class CarouselBase(VkObject):
    """VK Object WallCarouselBase

    carousel_offset - Index of current carousel element
    """

    carousel_offset: Optional[int] = None
