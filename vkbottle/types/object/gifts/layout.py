from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Layout(VkObject):
    """VK Object GiftsLayout

    build_id - ID of the build of constructor gift
    id - Gift ID
    is_stickers_style - Information whether gift represents a stickers style
    keywords - Keywords used for search
    stickers_product_id - ID of the sticker pack, if the gift is representing one
    thumb_256 - URL of the preview image with 256 px in width
    thumb_48 - URL of the preview image with 48 px in width
    thumb_512 - URL of the preview image with 512 px in width
    thumb_96 - URL of the preview image with 96 px in width
    """

    build_id: Optional[str] = None
    id: Optional[int] = None
    is_stickers_style: Optional[bool] = None
    keywords: Optional[str] = None
    stickers_product_id: Optional[int] = None
    thumb_256: Optional[str] = None
    thumb_48: Optional[str] = None
    thumb_512: Optional[str] = None
    thumb_96: Optional[str] = None
