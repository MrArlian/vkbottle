from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..photos.photo import Photo


class MarketAlbum(VkObject):
    """VK Object MarketMarketAlbum

    count - Items number
    id - Market album ID
    is_hidden - Is album hidden
    is_main - Is album main for owner
    owner_id - Market album owner's ID
    photo -
    title - Market album title
    updated_time - Date when album has been updated last time in Unixtime
    """

    count: int
    id: int
    is_hidden: Optional[bool] = None
    is_main: Optional[bool] = None
    owner_id: int
    photo: Optional[Photo] = None
    title: str
    updated_time: int
