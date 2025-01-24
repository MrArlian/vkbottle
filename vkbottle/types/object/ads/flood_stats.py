from __future__ import annotations

from ...base import VkObject


class FloodStats(VkObject):
    """VK Object AdsFloodStats

    left - Requests left
    refresh - Time to refresh in seconds
    """

    left: int
    refresh: int
