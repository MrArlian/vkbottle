from __future__ import annotations

from ...base import VkObject


class Section(VkObject):
    """VK Object MarketSection

    id - Section ID
    name - Section name
    """

    id: int
    name: str
