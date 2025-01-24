from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .conversation import Conversation
    from .message import Message


class ConversationWithMessage(VkObject):
    """VK Object MessagesConversationWithMessage"""

    conversation: Conversation
    last_message: Optional[Message] = None
