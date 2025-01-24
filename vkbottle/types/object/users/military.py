from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Military(VkObject):
    """VK Object UsersMilitary

    country_id - Country ID
    _from - From year
    id - Military ID
    unit - Unit name
    unit_id - Unit ID
    until - Till year
    """

    country_id: int
    _from: Optional[int] = None
    id: Optional[int] = None
    unit: str
    unit_id: int
    until: Optional[int] = None
