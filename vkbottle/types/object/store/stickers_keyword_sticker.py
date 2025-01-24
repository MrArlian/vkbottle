from __future__ import annotations

from ...base import VkObject


class StickersKeywordSticker(VkObject):
    """VK Object StoreStickersKeywordSticker

    pack_id - Pack id
    sticker_id - Sticker id
    """

    pack_id: int
    sticker_id: int
