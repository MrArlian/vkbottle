from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatLine(VkObject):
    """VK Object StoriesStatLine"""

    counter: Optional[int] = None
    is_unavailable: Optional[bool] = None
    name: str
