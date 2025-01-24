from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..wall.comment_attachment import CommentAttachment
    from ..base_likes_info import BaseLikesInfo


class TopicComment(VkObject):
    """VK Object BoardTopicComment

    attachments -
    can_edit - Information whether current user can edit the comment
    date - Date when the comment has been added in Unixtime
    from_id - Author ID
    id - Comment ID
    likes -
    real_offset - Real position of the comment
    text - Comment text
    """

    attachments: Optional[List[CommentAttachment]] = None
    can_edit: Optional[bool] = None
    date: int
    from_id: int
    id: int
    likes: Optional[BaseLikesInfo] = None
    real_offset: Optional[int] = None
    text: str
