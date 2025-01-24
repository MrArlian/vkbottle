from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .stats_city import StatsCity
    from .stats_sex_age import StatsSexAge
    from .stats_country import StatsCountry


class StatsExtended(VkObject):
    """VK Object UtilsStatsExtended

    cities -
    countries -
    sex_age -
    timestamp - Start time
    views - Total views number
    """

    cities: Optional[List[StatsCity]] = None
    countries: Optional[List[StatsCountry]] = None
    sex_age: Optional[List[StatsSexAge]] = None
    timestamp: Optional[int] = None
    views: Optional[int] = None
