from __future__ import annotations

from ..base import VkObject


class BaseGeoCoordinates(VkObject):
    """VK Object BaseGeoCoordinates"""

    latitude: float
    longitude: float
