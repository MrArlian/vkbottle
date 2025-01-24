from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .stats_cities import StatsCities
    from .stats_age import StatsAge
    from .stats_sex_age import StatsSexAge
    from .stats_sex import StatsSex


class DemostatsFormat(VkObject):
    """VK Object AdsDemostatsFormat

    age -
    cities -
    day - Day as YYYY-MM-DD
    month - Month as YYYY-MM
    overall - 1 if period=overall
    sex -
    sex_age -
    """

    age: Optional[List[StatsAge]] = None
    cities: Optional[List[StatsCities]] = None
    day: Optional[str] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    sex: Optional[List[StatsSex]] = None
    sex_age: Optional[List[StatsSexAge]] = None
