from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_reposts_info import BaseRepostsInfo
    from .comment_replies import CommentReplies
    from ..users.user_full import UserFull
    from ..wall.comment_attachment import CommentAttachment
    from ..wall.post_source import PostSource
    from .comment_media import CommentMedia
    from ..base_likes_info import BaseLikesInfo


class WidgetComment(VkObject):
    """VK Object WidgetsWidgetComment

    attachments -
    can_delete - Information whether current user can delete the comment
    comments -
    date - Date when the comment has been added in Unixtime
    from_id - Comment author ID
    id - Comment ID
    likes -
    media -
    post_source -
    post_type - Post type
    reposts -
    text - Comment text
    to_id - Wall owner
    user -
    """

    attachments: Optional[List[CommentAttachment]] = None
    can_delete: Optional[bool] = None
    comments: Optional[CommentReplies] = None
    date: int
    from_id: int
    id: int
    likes: Optional[BaseLikesInfo] = None
    media: Optional[CommentMedia] = None
    post_source: Optional[PostSource] = None
    post_type: int
    reposts: Optional[BaseRepostsInfo] = None
    text: str
    to_id: int
    user: Optional[UserFull] = None
