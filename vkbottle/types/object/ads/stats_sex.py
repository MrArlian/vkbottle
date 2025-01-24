from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AdsStatsSexValue

from ...base import VkObject


class StatsSex(VkObject):
    """VK Object AdsStatsSex

    clicks_rate - Clicks rate
    impressions_rate - Impressions rate
    value -
    """

    clicks_rate: Optional[float] = None
    impressions_rate: Optional[float] = None
    value: Optional[AdsStatsSexValue] = None
