from __future__ import annotations

from ..base import VkObject


class BaseObject(VkObject):
    """VK Object BaseObject

    id - Object ID
    title - Object title
    """

    id: int
    title: str
