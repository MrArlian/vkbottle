from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import ProductType

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_image import BaseImage
    from ..base_sticker_new import BaseStickerNew


class Product(VkObject):
    """VK Object StoreProduct

    active - Information whether the product is active (1 - yes, 0 - no)
    has_animation - Information whether the product is an animated sticker pack (for stickers product type)
    icon - Array of icon images or icon set object of the product (for stickers product type)
    id - Id of the product
    is_new - Information whether sticker product wasn't used after being purchased
    payment_region -
    previews - Array of preview images of the product (for stickers product type)
    promoted - Information whether the product is promoted (1 - yes, 0 - no)
    purchase_date - Date (Unix time) when the product was purchased
    purchased - Information whether the product is purchased (1 - yes, 0 - no)
    stickers -
    style_sticker_ids - Array of style sticker ids (for sticker pack styles)
    subtitle - Subtitle of the product
    title - Title of the product
    type - Product type
    """

    active: Optional[bool] = None
    has_animation: Optional[bool] = None
    icon: Optional[BaseImage] = None
    id: int
    is_new: Optional[bool] = None
    payment_region: Optional[str] = None
    previews: Optional[List[BaseImage]] = None
    promoted: Optional[bool] = None
    purchase_date: Optional[int] = None
    purchased: Optional[bool] = None
    stickers: Optional[BaseStickerNew] = None
    style_sticker_ids: Optional[List[int]] = None
    subtitle: Optional[str] = None
    title: Optional[str] = None
    type: ProductType
