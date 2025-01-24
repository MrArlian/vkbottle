from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ConversationCanWrite(VkObject):
    """VK Object MessagesConversationCanWrite"""

    allowed: bool
    reason: Optional[int] = None
