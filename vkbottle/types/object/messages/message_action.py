from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import MessagesMessageActionStatus

from ...base import VkObject

if TYPE_CHECKING:
    from .message_action_photo import MessageActionPhoto


class MessageAction(VkObject):
    """VK Object MessagesMessageAction

    conversation_message_id - Message ID
    email - Email address for chat_invite_user or chat_kick_user actions
    member_id - User or email peer ID
    message - Message body of related message
    photo -
    text - New chat title for chat_create and chat_title_update actions
    type -
    """

    conversation_message_id: Optional[int] = None
    email: Optional[str] = None
    member_id: Optional[int] = None
    message: Optional[str] = None
    photo: Optional[MessageActionPhoto] = None
    text: Optional[str] = None
    type: MessagesMessageActionStatus
