from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .base_sticker_animation import BaseStickerAnimation
    from .base_image import BaseImage


class BaseStickerNew(VkObject):
    """VK Object BaseStickerNew

    animation_url - URL of sticker animation script
    animations - Array of sticker animation script objects
    images -
    images_with_background -
    is_allowed - Information whether the sticker is allowed
    product_id - Pack ID
    sticker_id - Sticker ID
    """

    animation_url: Optional[str] = None
    animations: Optional[List[BaseStickerAnimation]] = None
    images: Optional[List[BaseImage]] = None
    images_with_background: Optional[List[BaseImage]] = None
    is_allowed: Optional[bool] = None
    product_id: Optional[int] = None
    sticker_id: Optional[int] = None
