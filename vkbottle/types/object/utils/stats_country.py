from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsCountry(VkObject):
    """VK Object UtilsStatsCountry

    country_id - Country ID
    views - Views number
    """

    country_id: Optional[int] = None
    views: Optional[int] = None
