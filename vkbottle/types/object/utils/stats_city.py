from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsCity(VkObject):
    """VK Object UtilsStatsCity

    city_id - City ID
    views - Views number
    """

    city_id: Optional[int] = None
    views: Optional[int] = None
