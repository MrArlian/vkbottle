from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Reply(VkObject):
    """VK Object NotificationsReply

    date - Date when the reply has been created in Unixtime
    id - Reply ID
    text - Reply text
    """

    date: Optional[int] = None
    id: Optional[int] = None
    text: Optional[int] = None
