from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .sex_age import SexAge
    from .country import Country
    from .city import City


class Reach(VkObject):
    """VK Object StatsReach

    age -
    cities -
    countries -
    mobile_reach - Reach count from mobile devices
    reach - Reach count
    reach_subscribers - Subscribers reach count
    sex -
    sex_age -
    """

    age: Optional[List[SexAge]] = None
    cities: Optional[List[City]] = None
    countries: Optional[List[Country]] = None
    mobile_reach: Optional[int] = None
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    sex: Optional[List[SexAge]] = None
    sex_age: Optional[List[SexAge]] = None
