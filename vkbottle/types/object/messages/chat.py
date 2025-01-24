from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .chat_push_settings import ChatPushSettings


class Chat(VkObject):
    """VK Object MessagesChat

    admin_id - Chat creator ID
    id - Chat ID
    is_default_photo - If provided photo is default
    is_group_channel - If chat is group channel
    kicked - Shows that user has been kicked from the chat
    left - Shows that user has been left the chat
    members_count - Count members in a chat
    photo_100 - URL of the preview image with 100 px in width
    photo_200 - URL of the preview image with 200 px in width
    photo_50 - URL of the preview image with 50 px in width
    push_settings -
    title - Chat title
    type - Chat type
    users -
    """

    admin_id: int
    id: int
    is_default_photo: Optional[bool] = None
    is_group_channel: Optional[bool] = None
    kicked: Optional[bool] = None
    left: Optional[bool] = None
    members_count: int
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional[ChatPushSettings] = None
    title: Optional[str] = None
    type: str
    users: List[int]
