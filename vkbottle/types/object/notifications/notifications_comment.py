from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..photos.photo import Photo
    from ..wall.wallpost import Wallpost
    from ..board.topic import Topic
    from ..video.video import Video


class NotificationsComment(VkObject):
    """VK Object NotificationsNotificationsComment

    date - Date when the comment has been added in Unixtime
    id - Comment ID
    owner_id - Author ID
    photo -
    post -
    text - Comment text
    topic -
    video -
    """

    date: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo: Optional[Photo] = None
    post: Optional[Wallpost] = None
    text: Optional[str] = None
    topic: Optional[Topic] = None
    video: Optional[Video] = None
