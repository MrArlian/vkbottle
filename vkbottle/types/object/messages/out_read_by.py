from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class OutReadBy(VkObject):
    """VK Object MessagesOutReadBy"""

    count: Optional[int] = None
    member_ids: Optional[List[int]] = None
