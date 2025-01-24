from __future__ import annotations

from ..base import VkObject


class BaseObjectWithName(VkObject):
    """VK Object BaseObjectWithName

    id - Object ID
    name - Object name
    """

    id: int
    name: str
