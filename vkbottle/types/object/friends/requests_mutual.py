from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class RequestsMutual(VkObject):
    """VK Object FriendsRequestsMutual

    count - Total mutual friends number
    users -
    """

    count: Optional[int] = None
    users: Optional[List[int]] = None
