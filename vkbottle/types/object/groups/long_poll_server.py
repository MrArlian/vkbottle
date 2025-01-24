from __future__ import annotations

from ...base import VkObject


class LongPollServer(VkObject):
    """VK Object GroupsLongPollServer

    key - Long Poll key
    server - Long Poll server address
    ts - Number of the last event
    """

    key: str
    server: str
    ts: str
