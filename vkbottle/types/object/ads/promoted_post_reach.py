from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PromotedPostReach(VkObject):
    """VK Object AdsPromotedPostReach

    hide - Hides amount
    id - Object ID from 'ids' parameter
    join_group - Community joins
    links - Link clicks
    reach_subscribers - Subscribers reach
    reach_total - Total reach
    report - Reports amount
    to_group - Community clicks
    unsubscribe - 'Unsubscribe' events amount
    video_views_100p - Video views for 100 percent
    video_views_25p - Video views for 25 percent
    video_views_3s - Video views for 3 seconds
    video_views_50p - Video views for 50 percent
    video_views_75p - Video views for 75 percent
    video_views_start - Video starts
    """

    hide: int
    id: int
    join_group: int
    links: int
    reach_subscribers: int
    reach_total: int
    report: int
    to_group: int
    unsubscribe: int
    video_views_100p: Optional[int] = None
    video_views_25p: Optional[int] = None
    video_views_3s: Optional[int] = None
    video_views_50p: Optional[int] = None
    video_views_75p: Optional[int] = None
    video_views_start: Optional[int] = None
