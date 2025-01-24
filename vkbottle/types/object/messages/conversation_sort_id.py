from __future__ import annotations

from ...base import VkObject


class ConversationSortId(VkObject):
    """VK Object MessagesConversationSortId

    major_id - Major id for sorting conversations
    minor_id - Minor id for sorting conversations
    """

    major_id: int
    minor_id: int
