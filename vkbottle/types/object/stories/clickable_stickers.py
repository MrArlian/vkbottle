from __future__ import annotations

from typing import TYPE_CHECKING, List

from ...base import VkObject

if TYPE_CHECKING:
    from .clickable_sticker import ClickableSticker


class ClickableStickers(VkObject):
    """VK Object StoriesClickableStickers"""

    clickable_stickers: List[ClickableSticker]
    original_height: int
    original_width: int
