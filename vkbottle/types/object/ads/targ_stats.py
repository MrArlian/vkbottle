from __future__ import annotations

from typing import Optional

from ...base import VkObject


class TargStats(VkObject):
    """VK Object AdsTargStats

    audience_count - Audience
    recommended_cpc - Recommended CPC value for 50% reach (old format)
    recommended_cpc_50 - Recommended CPC value for 50% reach
    recommended_cpc_70 - Recommended CPC value for 70% reach
    recommended_cpc_90 - Recommended CPC value for 90% reach
    recommended_cpm - Recommended CPM value for 50% reach (old format)
    recommended_cpm_50 - Recommended CPM value for 50% reach
    recommended_cpm_70 - Recommended CPM value for 70% reach
    recommended_cpm_90 - Recommended CPM value for 90% reach
    """

    audience_count: int
    recommended_cpc: Optional[float] = None
    recommended_cpc_50: Optional[float] = None
    recommended_cpc_70: Optional[float] = None
    recommended_cpc_90: Optional[float] = None
    recommended_cpm: Optional[float] = None
    recommended_cpm_50: Optional[float] = None
    recommended_cpm_70: Optional[float] = None
    recommended_cpm_90: Optional[float] = None
