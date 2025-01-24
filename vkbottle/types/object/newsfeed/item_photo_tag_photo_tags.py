from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .newsfeed_photo import NewsfeedPhoto


class ItemPhotoTagPhotoTags(VkObject):
    """VK Object NewsfeedItemPhotoTagPhotoTags

    count - Tags number
    items -
    """

    count: Optional[int] = None
    items: Optional[List[NewsfeedPhoto]] = None
