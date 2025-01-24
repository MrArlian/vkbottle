from __future__ import annotations

from typing import Union, Optional

from vkbottle.enum.vk_object import AdsAdStatus, AdsAdApproved, AdsAdCostType

from ...base import VkObject


class Ad(VkObject):
    """VK Object AdsAd

    ad_format - Ad format
    ad_platform - Ad platform
    all_limit - Total limit
    approved -
    autobidding_max_cost - Max cost of target actions for autobidding, kopecks
    campaign_id - Campaign ID
    category1_id - Category ID
    category2_id - Additional category ID
    cost_type -
    cpa - Cost of an action, kopecks
    cpc - Cost of a click, kopecks
    cpm - Cost of 1000 impressions, kopecks
    disclaimer_medical - Information whether disclaimer is enabled
    disclaimer_specialist - Information whether disclaimer is enabled
    disclaimer_supplements - Information whether disclaimer is enabled
    id - Ad ID
    impressions_limit - Impressions limit
    impressions_limited - Information whether impressions are limited
    name - Ad title
    ocpm - Cost of 1000 impressions optimized, kopecks
    status -
    video - Information whether the ad is a video
    """

    ad_format: int
    ad_platform: Optional[Union[int, str]] = None
    all_limit: int
    approved: AdsAdApproved
    autobidding_max_cost: Optional[int] = None
    campaign_id: int
    category1_id: Optional[int] = None
    category2_id: Optional[int] = None
    cost_type: AdsAdCostType
    cpa: Optional[int] = None
    cpc: Optional[int] = None
    cpm: Optional[int] = None
    disclaimer_medical: Optional[bool] = None
    disclaimer_specialist: Optional[bool] = None
    disclaimer_supplements: Optional[bool] = None
    id: int
    impressions_limit: Optional[int] = None
    impressions_limited: Optional[bool] = None
    name: str
    ocpm: Optional[int] = None
    status: AdsAdStatus
    video: Optional[bool] = None
