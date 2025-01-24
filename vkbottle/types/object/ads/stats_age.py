from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsAge(VkObject):
    """VK Object AdsStatsAge

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value - Age interval
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[str] = None
