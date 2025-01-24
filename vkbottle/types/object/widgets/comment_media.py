from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import WidgetsCommentMediaType

from ...base import VkObject


class CommentMedia(VkObject):
    """VK Object WidgetsCommentMedia

    item_id - Media item ID
    owner_id - Media owner's ID
    thumb_src - URL of the preview image (type=photo only)
    type -
    """

    item_id: Optional[int] = None
    owner_id: Optional[int] = None
    thumb_src: Optional[str] = None
    type: Optional[WidgetsCommentMediaType] = None
