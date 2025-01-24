from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .widget_likes import WidgetLikes
    from ..users.user_full import UserFull


class CommentRepliesItem(VkObject):
    """VK Object WidgetsCommentRepliesItem

    cid - Comment ID
    date - Date when the comment has been added in Unixtime
    likes -
    text - Comment text
    uid - User ID
    user -
    """

    cid: Optional[int] = None
    date: Optional[int] = None
    likes: Optional[WidgetLikes] = None
    text: Optional[str] = None
    uid: Optional[int] = None
    user: Optional[UserFull] = None
