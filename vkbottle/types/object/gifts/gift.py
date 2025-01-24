from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import GiftsGiftPrivacy

from ...base import VkObject

if TYPE_CHECKING:
    from .layout import Layout


class Gift(VkObject):
    """VK Object GiftsGift

    date - Date when gist has been sent in Unixtime
    from_id - Gift sender ID
    gift -
    gift_hash - Hash
    id - Gift ID
    message - Comment text
    privacy -
    """

    date: Optional[int] = None
    from_id: Optional[int] = None
    gift: Optional[Layout] = None
    gift_hash: Optional[str] = None
    id: Optional[int] = None
    message: Optional[str] = None
    privacy: Optional[GiftsGiftPrivacy] = None
