from __future__ import annotations

from ...base import VkObject


class SetCounterItem(VkObject):
    """VK Object SecureSetCounterItem

    id - User ID
    result -
    """

    id: int
    result: bool
