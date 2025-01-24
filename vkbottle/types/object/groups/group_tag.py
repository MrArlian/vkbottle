from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import GroupsGroupTagColor

from ...base import VkObject


class GroupTag(VkObject):
    """VK Object GroupsGroupTag"""

    color: GroupsGroupTagColor
    id: int
    name: str
    uses: Optional[int] = None
