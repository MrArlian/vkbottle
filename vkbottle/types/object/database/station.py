from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Station(VkObject):
    """VK Object DatabaseStation

    city_id - City ID
    color - Hex color code without #
    id - Station ID
    name - Station name
    """

    city_id: Optional[int] = None
    color: Optional[str] = None
    id: int
    name: str
