from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import NewsfeedItemDigestFullItemStyle

from ...base import VkObject

if TYPE_CHECKING:
    from ..wall.wallpost_attachment import WallpostAttachment
    from ..wall.wallpost import Wallpost


class ItemDigestFullItem(VkObject):
    """VK Object NewsfeedItemDigestFullItem"""

    attachment: Optional[WallpostAttachment] = None
    attachment_index: Optional[int] = None
    post: Wallpost
    source_name: Optional[str] = None
    style: Optional[NewsfeedItemDigestFullItemStyle] = None
    text: Optional[str] = None
