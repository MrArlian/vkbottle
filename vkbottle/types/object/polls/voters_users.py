from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class VotersUsers(VkObject):
    """VK Object PollsVotersUsers

    count - Votes number
    items -
    """

    count: Optional[int] = None
    items: Optional[List[int]] = None
