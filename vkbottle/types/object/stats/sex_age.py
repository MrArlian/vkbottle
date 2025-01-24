from __future__ import annotations

from typing import Optional

from ...base import VkObject


class SexAge(VkObject):
    """VK Object StatsSexAge

    count - Visitors number
    count_subscribers -
    reach -
    reach_subscribers -
    value - Sex/age value
    """

    count: Optional[int] = None
    count_subscribers: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    value: str
