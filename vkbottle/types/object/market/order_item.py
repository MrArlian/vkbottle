from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..photos.photo import Photo
    from .market_item import MarketItem
    from .price import Price


class OrderItem(VkObject):
    """VK Object MarketOrderItem"""

    item: MarketItem
    item_id: int
    owner_id: int
    photo: Optional[Photo] = None
    price: Price
    quantity: int
    title: Optional[str] = None
    variants: Optional[List[str]] = None
