from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .category import Category


class Category(VkObject):
    """VK Object AdsCategory

    id - Category ID
    name - Category name
    subcategories -
    """

    id: int
    name: str
    subcategories: Optional[List[Category]] = None
