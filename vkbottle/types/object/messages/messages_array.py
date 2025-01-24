from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .message import Message


class MessagesArray(VkObject):
    """VK Object MessagesMessagesArray"""

    count: Optional[int] = None
    items: Optional[List[Message]] = None
