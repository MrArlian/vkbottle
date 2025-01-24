from __future__ import annotations

from typing import Optional

from ..base import VkObject


class AdswebGetAdUnitsResponseAdUnitsAdUnit(VkObject):
    """VK Object AdswebGetAdUnitsResponseAdUnitsAdUnit"""

    id: int
    name: Optional[str] = None
    site_id: int
