from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsSexAge(VkObject):
    """VK Object AdsStatsSexAge

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value - Sex and age interval
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[str] = None
