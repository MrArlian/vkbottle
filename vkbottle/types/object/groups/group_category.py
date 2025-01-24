from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_object_with_name import BaseObjectWithName


class GroupCategory(VkObject):
    """VK Object GroupsGroupCategory

    id - Category ID
    name - Category name
    subcategories -
    """

    id: int
    name: str
    subcategories: Optional[List[BaseObjectWithName]] = None
