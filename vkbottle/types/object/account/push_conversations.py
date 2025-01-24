from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .push_conversations_item import PushConversationsItem


class PushConversations(VkObject):
    """VK Object AccountPushConversations

    count - Items count
    items -
    """

    count: Optional[int] = None
    items: Optional[List[PushConversationsItem]] = None
