from __future__ import annotations

from typing import Optional

from ...base import VkObject


class City(VkObject):
    """VK Object StatsCity

    count - Visitors number
    name - City name
    value - City ID
    """

    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None
