from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Career(VkObject):
    """VK Object UsersCareer

    city_id - City ID
    city_name - City name
    company - Company name
    country_id - Country ID
    _from - From year
    group_id - Community ID
    id - Career ID
    position - Position
    until - Till year
    """

    city_id: Optional[int] = None
    city_name: Optional[str] = None
    company: Optional[str] = None
    country_id: Optional[int] = None
    _from: Optional[int] = None
    group_id: Optional[int] = None
    id: Optional[int] = None
    position: Optional[str] = None
    until: Optional[int] = None
