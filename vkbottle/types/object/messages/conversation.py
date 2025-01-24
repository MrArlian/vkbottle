from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import MessagesConversationSpecialServiceType

from ...base import VkObject

if TYPE_CHECKING:
    from .chat_settings import ChatSettings
    from .message_request_data import MessageRequestData
    from .keyboard import Keyboard
    from .conversation_sort_id import ConversationSortId
    from .push_settings import PushSettings
    from .out_read_by import OutReadBy
    from .conversation_peer import ConversationPeer
    from .conversation_can_write import ConversationCanWrite


class Conversation(VkObject):
    """VK Object MessagesConversation

    can_write -
    chat_settings -
    current_keyboard -
    important -
    in_read - Last message user have read
    is_marked_unread - Is this conversation uread
    last_conversation_message_id - Conversation message ID of the last message in conversation
    last_message_id - ID of the last message in conversation
    mentions - Ids of messages with mentions
    message_request_data -
    out_read - Last outcoming message have been read by the opponent
    out_read_by -
    peer -
    push_settings -
    sort_id -
    special_service_type -
    unanswered -
    unread_count - Unread messages number
    """

    can_write: Optional[ConversationCanWrite] = None
    chat_settings: Optional[ChatSettings] = None
    current_keyboard: Optional[Keyboard] = None
    important: Optional[bool] = None
    in_read: int
    is_marked_unread: Optional[bool] = None
    last_conversation_message_id: Optional[int] = None
    last_message_id: int
    mentions: Optional[List[int]] = None
    message_request_data: Optional[MessageRequestData] = None
    out_read: int
    out_read_by: Optional[OutReadBy] = None
    peer: ConversationPeer
    push_settings: Optional[PushSettings] = None
    sort_id: Optional[ConversationSortId] = None
    special_service_type: Optional[MessagesConversationSpecialServiceType] = None
    unanswered: Optional[bool] = None
    unread_count: Optional[int] = None
