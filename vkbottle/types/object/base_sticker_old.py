from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseStickerOld(VkObject):
    """VK Object BaseStickerOld

    height - Height in px
    id - Sticker ID
    is_allowed - Information whether the sticker is allowed
    photo_128 - URL of the preview image with 128 px in height
    photo_256 - URL of the preview image with 256 px in height
    photo_352 - URL of the preview image with 352 px in height
    photo_512 - URL of the preview image with 512 px in height
    photo_64 - URL of the preview image with 64 px in height
    product_id - Pack ID
    width - Width in px
    """

    height: Optional[int] = None
    id: Optional[int] = None
    is_allowed: Optional[bool] = None
    photo_128: Optional[str] = None
    photo_256: Optional[str] = None
    photo_352: Optional[str] = None
    photo_512: Optional[str] = None
    photo_64: Optional[str] = None
    product_id: Optional[int] = None
    width: Optional[int] = None
