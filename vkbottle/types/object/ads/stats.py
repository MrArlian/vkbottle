from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import AdsObjectType

from ...base import VkObject

if TYPE_CHECKING:
    from .stats_format import StatsFormat
    from .stats_views_times import StatsViewsTimes


class Stats(VkObject):
    """VK Object AdsStats

    id - Object ID
    stats -
    type -
    views_times -
    """

    id: Optional[int] = None
    stats: Optional[StatsFormat] = None
    type: Optional[AdsObjectType] = None
    views_times: Optional[StatsViewsTimes] = None
