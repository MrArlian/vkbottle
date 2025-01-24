from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_link import BaseLink
    from .order_item import OrderItem
    from .price import Price


class Order(VkObject):
    """VK Object MarketOrder

    address -
    cancel_info - Information for cancel and revert order
    comment -
    date -
    display_order_id -
    group_id -
    id -
    items_count -
    merchant_comment -
    preview_order_items - Several order items for preview
    status -
    total_price -
    track_link -
    track_number -
    user_id -
    weight -
    """

    address: Optional[str] = None
    cancel_info: Optional[BaseLink] = None
    comment: Optional[str] = None
    date: int
    display_order_id: Optional[str] = None
    group_id: int
    id: int
    items_count: int
    merchant_comment: Optional[str] = None
    preview_order_items: Optional[List[OrderItem]] = None
    status: int
    total_price: Price
    track_link: Optional[str] = None
    track_number: Optional[str] = None
    user_id: int
    weight: Optional[int] = None
