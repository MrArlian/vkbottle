from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AdsCampaignStatus, AdsCampaignType

from ...base import VkObject


class Campaign(VkObject):
    """VK Object AdsCampaign

    ads_count - Amount of active ads in campaign
    all_limit - Campaign's total limit, rubles
    create_time - Campaign create time, as Unixtime
    day_limit - Campaign's day limit, rubles
    goal_type - Campaign goal type
    id - Campaign ID
    is_cbo_enabled - Shows if Campaign Budget Optimization is on
    name - Campaign title
    start_time - Campaign start time, as Unixtime
    status -
    stop_time - Campaign stop time, as Unixtime
    type -
    update_time - Campaign update time, as Unixtime
    user_goal_type - Campaign user goal type
    views_limit - Limit of views per user per campaign
    """

    ads_count: Optional[int] = None
    all_limit: str
    create_time: Optional[int] = None
    day_limit: str
    goal_type: Optional[int] = None
    id: int
    is_cbo_enabled: Optional[bool] = None
    name: str
    start_time: int
    status: AdsCampaignStatus
    stop_time: int
    type: AdsCampaignType
    update_time: Optional[int] = None
    user_goal_type: Optional[int] = None
    views_limit: Optional[int] = None
