from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .market.price import Price


class BaseLinkProduct(VkObject):
    """VK Object BaseLinkProduct"""

    merchant: Optional[str] = None
    orders_count: Optional[int] = None
    price: Price
