from __future__ import annotations

from typing import TYPE_CHECKING, List

from ...base import VkObject

if TYPE_CHECKING:
    from .conversation import Conversation


class GetConversationById(VkObject):
    """VK Object MessagesGetConversationById

    count - Total number
    items -
    """

    count: int
    items: List[Conversation]
