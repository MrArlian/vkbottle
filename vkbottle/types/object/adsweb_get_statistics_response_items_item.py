from __future__ import annotations

from typing import Optional

from ..base import VkObject


class AdswebGetStatisticsResponseItemsItem(VkObject):
    """VK Object AdswebGetStatisticsResponseItemsItem"""

    ad_unit_id: Optional[int] = None
    day_max: Optional[str] = None
    day_min: Optional[str] = None
    days_count: Optional[int] = None
    hour_max: Optional[str] = None
    hour_min: Optional[str] = None
    hours_count: Optional[int] = None
    month_max: Optional[str] = None
    month_min: Optional[str] = None
    months_count: Optional[int] = None
    overall_count: Optional[int] = None
    site_id: Optional[int] = None
