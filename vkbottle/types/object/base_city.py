from __future__ import annotations

from ..base import VkObject


class BaseCity(VkObject):
    """VK Object BaseCity

    id - City ID
    title - City title
    """

    id: int
    title: str
