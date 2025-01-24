from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .base_place import BasePlace
    from .base_geo_coordinates import BaseGeoCoordinates


class BaseGeo(VkObject):
    """VK Object BaseGeo

    coordinates -
    place -
    showmap - Information whether a map is showed
    type - Place type
    """

    coordinates: Optional[BaseGeoCoordinates] = None
    place: Optional[BasePlace] = None
    showmap: Optional[int] = None
    type: Optional[str] = None
