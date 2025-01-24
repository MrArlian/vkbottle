from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .comment_replies_item import CommentRepliesItem


class CommentReplies(VkObject):
    """VK Object WidgetsCommentReplies

    can_post - Information whether current user can comment the post
    count - Comments number
    replies -
    """

    can_post: Optional[bool] = None
    count: Optional[int] = None
    replies: Optional[List[CommentRepliesItem]] = None
