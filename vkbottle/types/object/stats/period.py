from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .reach import Reach
    from .views import Views
    from .activity import Activity


class Period(VkObject):
    """VK Object StatsPeriod

    activity -
    period_from - Unix timestamp
    period_to - Unix timestamp
    reach -
    visitors -
    """

    activity: Optional[Activity] = None
    period_from: Optional[int] = None
    period_to: Optional[int] = None
    reach: Optional[Reach] = None
    visitors: Optional[Views] = None
