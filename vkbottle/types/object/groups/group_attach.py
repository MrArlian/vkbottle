from __future__ import annotations

from ...base import VkObject


class GroupAttach(VkObject):
    """VK Object GroupsGroupAttach

    id - group ID
    is_favorite - is favorite
    size - size of group
    status - activity or category of group
    text - text of attach
    """

    id: int
    is_favorite: bool
    size: int
    status: str
    text: str
