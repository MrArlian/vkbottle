from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..photos import Photo

if TYPE_CHECKING:
    from ..base_object_count import BaseObjectCount
    from ..base_likes import BaseLikes


class NewsfeedPhoto(Photo):
    """VK Object NewsfeedNewsfeedPhoto

    can_repost - Information whether current user can repost the photo
    comments -
    likes -
    """

    can_repost: Optional[bool] = None
    comments: Optional[BaseObjectCount] = None
    likes: Optional[BaseLikes] = None

