from __future__ import annotations

from typing import Optional

from ...base import VkObject


class WidgetLikes(VkObject):
    """VK Object WidgetsWidgetLikes

    count - Likes number
    """

    count: Optional[int] = None
