from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import WallPostType

from ...base import VkObject

if TYPE_CHECKING:
    from .wallpost_attachment import WallpostAttachment
    from ..base_reposts_info import BaseRepostsInfo
    from .geo import Geo
    from .post_source import PostSource
    from .views import Views
    from .post_copyright import PostCopyright
    from ..base_likes_info import BaseLikesInfo


class Wallpost(VkObject):
    """VK Object WallWallpost

    access_key - Access key to private object
    attachments -
    copyright - Information about the source of the post
    date - Date of publishing in Unixtime
    edited - Date of editing in Unixtime
    from_id - Post author ID
    geo -
    id - Post ID
    is_archived - Is post archived, only for post owners
    is_deleted -
    is_favorite - Information whether the post in favorites list
    likes - Count of likes
    owner_id - Wall owner's ID
    parents_stack - If post type 'reply', contains original parent IDs stack
    post_id - If post type 'reply', contains original post ID
    post_source -
    post_type -
    reposts -
    signer_id - Post signer ID
    text - Post text
    views - Count of views
    """

    access_key: Optional[str] = None
    attachments: Optional[List[WallpostAttachment]] = None
    copyright: Optional[PostCopyright] = None
    date: Optional[int] = None
    edited: Optional[int] = None
    from_id: Optional[int] = None
    geo: Optional[Geo] = None
    id: Optional[int] = None
    is_archived: Optional[bool] = None
    is_deleted: Optional[bool] = None
    is_favorite: Optional[bool] = None
    likes: Optional[BaseLikesInfo] = None
    owner_id: Optional[int] = None
    parents_stack: Optional[List[int]] = None
    post_id: Optional[int] = None
    post_source: Optional[PostSource] = None
    post_type: Optional[WallPostType] = None
    reposts: Optional[BaseRepostsInfo] = None
    signer_id: Optional[int] = None
    text: Optional[str] = None
    views: Optional[Views] = None
