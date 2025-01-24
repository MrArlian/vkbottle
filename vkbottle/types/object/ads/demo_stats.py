from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import AdsObjectType

from ...base import VkObject

if TYPE_CHECKING:
    from .demostats_format import DemostatsFormat


class DemoStats(VkObject):
    """VK Object AdsDemoStats

    id - Object ID
    stats -
    type -
    """

    id: Optional[int] = None
    stats: Optional[DemostatsFormat] = None
    type: Optional[AdsObjectType] = None
