from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .group_category import GroupCategory
    from .group import Group


class GroupCategoryFull(VkObject):
    """VK Object GroupsGroupCategoryFull

    id - Category ID
    name - Category name
    page_count - Pages number
    page_previews -
    subcategories -
    """

    id: int
    name: str
    page_count: int
    page_previews: List[Group]
    subcategories: Optional[List[GroupCategory]] = None
