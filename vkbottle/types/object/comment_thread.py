from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .wall.wall_comment import WallComment


class CommentThread(VkObject):
    """VK Object CommentThread

    can_post - Information whether current user can comment the post
    count - Comments number
    groups_can_post - Information whether groups can comment the post
    items -
    show_reply_button - Information whether recommended to display reply button
    """

    can_post: Optional[bool] = None
    count: int
    groups_can_post: Optional[bool] = None
    items: Optional[List[WallComment]] = None
    show_reply_button: Optional[bool] = None
