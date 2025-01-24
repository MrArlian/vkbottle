from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .user_xtr_invited_by import UserXtrInvitedBy
    from .chat_push_settings import ChatPushSettings


class ChatFull(VkObject):
    """VK Object MessagesChatFull

    admin_id - Chat creator ID
    id - Chat ID
    kicked - Shows that user has been kicked from the chat
    left - Shows that user has been left the chat
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
    kicked: Optional[bool] = None
    left: Optional[bool] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional[ChatPushSettings] = None
    title: Optional[str] = None
    type: str
    users: List[UserXtrInvitedBy]
