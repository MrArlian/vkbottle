from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import MarketMarketItemAvailability

from ...base import VkObject

if TYPE_CHECKING:
    from .market_category import MarketCategory
    from .price import Price


class MarketItem(VkObject):
    """VK Object MarketMarketItem

    access_key - Access key for the market item
    availability -
    button_title - Title for button for url
    category -
    date - Date when the item has been created in Unixtime
    description - Item description
    external_id -
    id - Item ID
    is_favorite -
    is_main_variant -
    owner_id - Item owner's ID
    price -
    sku -
    thumb_photo - URL of the preview image
    title - Item title
    url - URL to item
    variants_grouping_id -
    """

    access_key: Optional[str] = None
    availability: MarketMarketItemAvailability
    button_title: Optional[str] = None
    category: MarketCategory
    date: Optional[int] = None
    description: str
    external_id: Optional[str] = None
    id: int
    is_favorite: Optional[bool] = None
    is_main_variant: Optional[bool] = None
    owner_id: int
    price: Price
    sku: Optional[str] = None
    thumb_photo: Optional[str] = None
    title: str
    url: Optional[str] = None
    variants_grouping_id: Optional[int] = None
