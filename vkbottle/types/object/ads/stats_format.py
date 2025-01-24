from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsFormat(VkObject):
    """VK Object AdsStatsFormat

    clicks - Clicks number
    day - Day as YYYY-MM-DD
    impressions - Impressions number
    join_rate - Events number
    link_external_clicks - External clicks number
    month - Month as YYYY-MM
    overall - 1 if period=overall
    reach - Reach
    spent - Spent funds
    video_clicks_site - Clickthoughs to the advertised site
    video_views - Video views number
    video_views_full - Video views (full video)
    video_views_half - Video views (half of video)
    """

    clicks: Optional[int] = None
    day: Optional[str] = None
    impressions: Optional[int] = None
    join_rate: Optional[int] = None
    link_external_clicks: Optional[int] = None
    month: Optional[str] = None
    overall: Optional[int] = None
    reach: Optional[int] = None
    spent: Optional[int] = None
    video_clicks_site: Optional[int] = None
    video_views: Optional[int] = None
    video_views_full: Optional[int] = None
    video_views_half: Optional[int] = None
