from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import FaveBookmarkType

from ...base import VkObject

if TYPE_CHECKING:
    from .tag import Tag
    from ..video.video_full import VideoFull
    from ..base_link import BaseLink
    from ..market.market_item import MarketItem
    from ..wall.wallpost_full import WallpostFull


class Bookmark(VkObject):
    """VK Object FaveBookmark

    added_date - Timestamp, when this item was bookmarked
    link -
    post -
    product -
    seen - Has user seen this item
    tags -
    type - Item type
    video -
    """

    added_date: int
    link: Optional[BaseLink] = None
    post: Optional[WallpostFull] = None
    product: Optional[MarketItem] = None
    seen: bool
    tags: List[Tag]
    type: FaveBookmarkType
    video: Optional[VideoFull] = None
