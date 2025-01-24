from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .sex_age import SexAge


class WallpostStat(VkObject):
    """VK Object StatsWallpostStat

    hide - Hidings number
    join_group - People have joined the group
    links - Link clickthrough
    post_id -
    reach_ads -
    reach_subscribers - Subscribers reach
    reach_subscribers_count -
    reach_total - Total reach
    reach_total_count -
    reach_viral -
    report - Reports number
    sex_age -
    to_group - Clickthrough to community
    unsubscribe - Unsubscribed members
    """

    hide: Optional[int] = None
    join_group: Optional[int] = None
    links: Optional[int] = None
    post_id: Optional[int] = None
    reach_ads: Optional[int] = None
    reach_subscribers: Optional[int] = None
    reach_subscribers_count: Optional[int] = None
    reach_total: Optional[int] = None
    reach_total_count: Optional[int] = None
    reach_viral: Optional[int] = None
    report: Optional[int] = None
    sex_age: Optional[List[SexAge]] = None
    to_group: Optional[int] = None
    unsubscribe: Optional[int] = None
