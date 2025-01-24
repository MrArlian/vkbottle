from __future__ import annotations

from ..base import VkObject


class BaseGradientPoint(VkObject):
    """VK Object BaseGradientPoint

    color - Hex color code without #
    position - Point position
    """

    color: str
    position: float
