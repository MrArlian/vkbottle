from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..market.currency import Currency
    from ..market.price import Price


class MarketInfo(VkObject):
    """VK Object GroupsMarketInfo

    contact_id - Contact person ID
    currency -
    currency_text - Currency name
    enabled - Information whether the market is enabled
    main_album_id - Main market album ID
    min_order_price -
    price_max - Maximum price
    price_min - Minimum price
    type - Market type
    """

    contact_id: Optional[int] = None
    currency: Optional[Currency] = None
    currency_text: Optional[str] = None
    enabled: Optional[bool] = None
    main_album_id: Optional[int] = None
    min_order_price: Optional[Price] = None
    price_max: Optional[str] = None
    price_min: Optional[str] = None
    type: Optional[str] = None
