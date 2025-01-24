from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class Forward(VkObject):
    """VK Object MessagesForward

    conversation_message_ids -
    is_reply - If you need to reply to a message
    message_ids -
    owner_id - Messages owner_id
    peer_id - Messages peer_id
    """

    conversation_message_ids: Optional[List[int]] = None
    is_reply: Optional[bool] = None
    message_ids: Optional[List[int]] = None
    owner_id: Optional[int] = None
    peer_id: Optional[int] = None
