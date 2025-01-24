from __future__ import annotations

from typing import List

from ...base import VkObject


class GroupsArray(VkObject):
    """VK Object GroupsGroupsArray

    count - Communities number
    items -
    """

    count: int
    items: List[int]
