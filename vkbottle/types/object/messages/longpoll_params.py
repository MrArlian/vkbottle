from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LongpollParams(VkObject):
    """VK Object MessagesLongpollParams

    key - Key
    pts - Persistent timestamp
    server - Server URL
    ts - Timestamp
    """

    key: str
    pts: Optional[int] = None
    server: str
    ts: int
