from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BasePlace(VkObject):
    """VK Object BasePlace

    address - Place address
    checkins - Checkins number
    city - City name
    country - Country name
    created - Date of the place creation in Unixtime
    icon - URL of the place's icon
    id - Place ID
    latitude - Place latitude
    longitude - Place longitude
    title - Place title
    type - Place type
    """

    address: Optional[str] = None
    checkins: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    created: Optional[int] = None
    icon: Optional[str] = None
    id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    title: Optional[str] = None
    type: Optional[str] = None
