from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .market_category_tree import MarketCategoryTree


class MarketCategoryTree(VkObject):
    """VK Object MarketMarketCategoryTree

    children -
    id - Category ID
    name - Category name
    """

    children: Optional[List[MarketCategoryTree]] = None
    id: int
    name: str
