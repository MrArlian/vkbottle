from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class Participants(VkObject):
    """VK Object CallsParticipants

    count - Participants count
    list -
    """

    count: Optional[int] = None
    list: Optional[List[int]] = None
