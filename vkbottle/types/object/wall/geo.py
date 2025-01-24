from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import PlaceType

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_place import BasePlace


class Geo(VkObject):
    """VK Object WallGeo

    coordinates - Coordinates as string. <latitude> <longtitude>
    place -
    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: Optional[str] = None
    place: Optional[BasePlace] = None
    showmap: Optional[int] = None
    type: Optional[PlaceType] = None
