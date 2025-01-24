from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LastSeen(VkObject):
    """VK Object UsersLastSeen

    platform - Type of the platform that used for the last authorization
    time - Last visit date (in Unix time)
    """

    platform: Optional[int] = None
    time: Optional[int] = None
