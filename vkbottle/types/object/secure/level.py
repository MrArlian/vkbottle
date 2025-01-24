from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Level(VkObject):
    """VK Object SecureLevel

    level - Level
    uid - User ID
    """

    level: Optional[int] = None
    uid: Optional[int] = None
