from __future__ import annotations

from ..base import VkObject


class BaseCropPhotoRect(VkObject):
    """VK Object BaseCropPhotoRect

    x - Coordinate X of the left upper corner
    x2 - Coordinate X of the right lower corner
    y - Coordinate Y of the left upper corner
    y2 - Coordinate Y of the right lower corner
    """

    x: float
    x2: float
    y: float
    y2: float
