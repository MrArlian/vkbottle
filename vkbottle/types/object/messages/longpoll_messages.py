from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .message import Message


class LongpollMessages(VkObject):
    """VK Object MessagesLongpollMessages

    count - Total number
    items -
    """

    count: Optional[int] = None
    items: Optional[List[Message]] = None
