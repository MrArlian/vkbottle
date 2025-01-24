from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Stats(VkObject):
    """VK Object UtilsStats

    timestamp - Start time
    views - Total views number
    """

    timestamp: Optional[int] = None
    views: Optional[int] = None
