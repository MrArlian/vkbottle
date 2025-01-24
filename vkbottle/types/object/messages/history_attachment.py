from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .history_message_attachment import HistoryMessageAttachment


class HistoryAttachment(VkObject):
    """VK Object MessagesHistoryAttachment

    attachment -
    forward_level - Forward level (optional)
    from_id - Message author's ID
    message_id - Message ID
    was_listened -
    """

    attachment: HistoryMessageAttachment
    forward_level: Optional[int] = None
    from_id: int
    message_id: int
    was_listened: Optional[bool] = None
