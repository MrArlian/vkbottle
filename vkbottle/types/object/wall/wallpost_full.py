from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from vkbottle.enum.vk_object import WallWallpostFullTopicId

from .carousel_base import CarouselBase
from .wallpost import Wallpost

if TYPE_CHECKING:
    from ..base_comments_info import BaseCommentsInfo
    from .wallpost_donut import WallpostDonut


class WallpostFull(CarouselBase, Wallpost):
    """VK Object WallWallpostFull

    can_delete - Information whether current user can delete the post
    can_edit - Information whether current user can edit the post
    can_pin - Information whether current user can pin the post
    comments -
    copy_history -
    created_by - Post creator ID (if post still can be edited)
    donut -
    hash - Hash for sharing
    is_pinned - Information whether the post is pinned
    marked_as_ads - Information whether the post is marked as ads
    short_text_rate - Preview length control parameter
    topic_id - Topic ID. Allowed values can be obtained from newsfeed.getPostTopics method
    """

    can_delete: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_pin: Optional[bool] = None
    comments: Optional[BaseCommentsInfo] = None
    copy_history: Optional[List[WallpostFull]] = None
    created_by: Optional[int] = None
    donut: Optional[WallpostDonut] = None
    hash: Optional[str] = None
    is_pinned: Optional[int] = None
    marked_as_ads: Optional[bool] = None
    short_text_rate: Optional[float] = None
    topic_id: Optional[WallWallpostFullTopicId] = None
