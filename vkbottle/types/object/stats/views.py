from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .sex_age import SexAge
    from .country import Country
    from .city import City


class Views(VkObject):
    """VK Object StatsViews

    age -
    cities -
    countries -
    mobile_views - Number of views from mobile devices
    sex -
    sex_age -
    views - Views number
    visitors - Visitors number
    """

    age: Optional[List[SexAge]] = None
    cities: Optional[List[City]] = None
    countries: Optional[List[Country]] = None
    mobile_views: Optional[int] = None
    sex: Optional[List[SexAge]] = None
    sex_age: Optional[List[SexAge]] = None
    views: Optional[int] = None
    visitors: Optional[int] = None
