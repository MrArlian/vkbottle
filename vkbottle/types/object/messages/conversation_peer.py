from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import MessagesConversationPeerType

from ...base import VkObject


class ConversationPeer(VkObject):
    """VK Object MessagesConversationPeer"""

    id: int
    local_id: Optional[int] = None
    type: MessagesConversationPeerType
