from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .market_category_nested import MarketCategoryNested


class MarketCategoryNested(VkObject):
    """VK Object MarketMarketCategoryNested

    id - Category ID
    name - Category name
    parent -
    """

    id: int
    name: str
    parent: Optional[MarketCategoryNested] = None
