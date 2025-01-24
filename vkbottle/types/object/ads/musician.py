from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Musician(VkObject):
    """VK Object AdsMusician

    avatar - Music artist photo
    id - Targeting music artist ID
    name - Music artist name
    """

    avatar: Optional[str] = None
    id: int
    name: str
