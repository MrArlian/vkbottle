from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LiveInfo(VkObject):
    """VK Object VideoLiveInfo"""

    enabled: bool
    is_notifications_blocked: Optional[bool] = None
