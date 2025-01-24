from __future__ import annotations

from typing import Optional

from ...base import VkObject


class MessageRequestData(VkObject):
    """VK Object MessagesMessageRequestData

    inviter_id - Message request sender id
    request_date - Message request date
    status - Status of message request
    """

    inviter_id: Optional[int] = None
    request_date: Optional[int] = None
    status: Optional[str] = None
