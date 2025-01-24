from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsCities(VkObject):
    """VK Object AdsStatsCities

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    name - City name
    value - City ID
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    name: Optional[str] = None
    value: Optional[int] = None
