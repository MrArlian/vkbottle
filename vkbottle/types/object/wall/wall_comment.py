from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .wall_comment_donut import WallCommentDonut
    from ..base_likes_info import BaseLikesInfo
    from .comment_attachment import CommentAttachment
    from ..comment_thread import CommentThread


class WallComment(VkObject):
    """VK Object WallWallComment

    attachments -
    can_edit -
    date - Date when the comment has been added in Unixtime
    deleted -
    donut -
    from_id - Author ID
    id - Comment ID
    likes -
    owner_id -
    parents_stack -
    photo_id -
    pid - Photo ID
    post_id -
    real_offset - Real position of the comment
    reply_to_comment - Replied comment ID
    reply_to_user - Replied user ID
    text - Comment text
    thread -
    video_id -
    """

    attachments: Optional[List[CommentAttachment]] = None
    can_edit: Optional[bool] = None
    date: int
    deleted: Optional[bool] = None
    donut: Optional[WallCommentDonut] = None
    from_id: int
    id: int
    likes: Optional[BaseLikesInfo] = None
    owner_id: Optional[int] = None
    parents_stack: Optional[List[int]] = None
    photo_id: Optional[int] = None
    pid: Optional[int] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: str
    thread: Optional[CommentThread] = None
    video_id: Optional[int] = None
