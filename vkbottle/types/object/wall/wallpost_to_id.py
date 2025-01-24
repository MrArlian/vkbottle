from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import WallPostType

from ...base import VkObject

if TYPE_CHECKING:
    from .wallpost_attachment import WallpostAttachment
    from ..base_reposts_info import BaseRepostsInfo
    from .geo import Geo
    from ..base_comments_info import BaseCommentsInfo
    from .post_source import PostSource
    from ..base_likes_info import BaseLikesInfo


class WallpostToId(VkObject):
    """VK Object WallWallpostToId

    attachments -
    comments -
    copy_owner_id - ID of the source post owner
    copy_post_id - ID of the source post
    date - Date of publishing in Unixtime
    from_id - Post author ID
    geo -
    id - Post ID
    is_favorite - Information whether the post in favorites list
    likes -
    post_id - wall post ID (if comment)
    post_source -
    post_type -
    reposts -
    signer_id - Post signer ID
    text - Post text
    to_id - Wall owner's ID
    """

    attachments: Optional[List[WallpostAttachment]] = None
    comments: Optional[BaseCommentsInfo] = None
    copy_owner_id: Optional[int] = None
    copy_post_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional[Geo] = None
    id: Optional[int] = None
    is_favorite: Optional[bool] = None
    likes: Optional[BaseLikesInfo] = None
    post_id: Optional[int] = None
    post_source: Optional[PostSource] = None
    post_type: Optional[WallPostType] = None
    reposts: Optional[BaseRepostsInfo] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    to_id: Optional[int] = None
