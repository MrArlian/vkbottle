from __future__ import annotations

from ...base import VkObject


class Value(VkObject):
    """VK Object StorageValue"""

    key: str
    value: str
