from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .wall.wallpost_comments_donut import WallpostCommentsDonut


class BaseCommentsInfo(VkObject):
    """VK Object BaseCommentsInfo

    can_close -
    can_open -
    can_post - Information whether current user can comment the post
    count - Comments number
    donut -
    groups_can_post - Information whether groups can comment the post
    """

    can_close: Optional[bool] = None
    can_open: Optional[bool] = None
    can_post: Optional[bool] = None
    count: Optional[int] = None
    donut: Optional[WallpostCommentsDonut] = None
    groups_can_post: Optional[bool] = None
