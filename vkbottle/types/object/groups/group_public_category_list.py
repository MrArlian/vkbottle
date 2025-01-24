from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .group_category_type import GroupCategoryType


class GroupPublicCategoryList(VkObject):
    """VK Object GroupsGroupPublicCategoryList"""

    id: Optional[int] = None
    name: Optional[str] = None
    subcategories: Optional[List[GroupCategoryType]] = None
