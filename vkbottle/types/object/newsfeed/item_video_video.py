from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..video.video import Video


class ItemVideoVideo(VkObject):
    """VK Object NewsfeedItemVideoVideo

    count - Tags number
    items -
    """

    count: Optional[int] = None
    items: Optional[List[Video]] = None
