from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AdsAdCostType

from ...base import VkObject


class AdLayout(VkObject):
    """VK Object AdsAdLayout

    ad_format - Ad format
    campaign_id - Campaign ID
    cost_type -
    description - Ad description
    id - Ad ID
    image_src - Image URL
    image_src_2x - URL of the preview image in double size
    link_domain - Domain of advertised object
    link_url - URL of advertised object
    preview_link - link to preview an ad as it is shown on the website
    title - Ad title
    video - Information whether the ad is a video
    """

    ad_format: int
    campaign_id: int
    cost_type: AdsAdCostType
    description: str
    id: str
    image_src: str
    image_src_2x: Optional[str] = None
    link_domain: Optional[str] = None
    link_url: str
    preview_link: Optional[str] = None
    title: str
    video: Optional[bool] = None
