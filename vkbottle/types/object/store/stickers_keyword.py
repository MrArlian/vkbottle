from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .stickers_keyword_sticker import StickersKeywordSticker
    from ..base_sticker_new import BaseStickerNew


class StickersKeyword(VkObject):
    """VK Object StoreStickersKeyword"""

    promoted_stickers: Optional[BaseStickerNew] = None
    stickers: Optional[List[StickersKeywordSticker]] = None
    user_stickers: Optional[BaseStickerNew] = None
    words: List[str]
