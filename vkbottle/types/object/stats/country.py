from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Country(VkObject):
    """VK Object StatsCountry

    code - Country code
    count - Visitors number
    name - Country name
    value - Country ID
    """

    code: Optional[str] = None
    count: Optional[int] = None
    name: Optional[str] = None
    value: Optional[int] = None
