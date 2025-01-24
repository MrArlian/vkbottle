from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Region(VkObject):
    """VK Object DatabaseRegion

    id - Region ID
    title - Region title
    """

    id: Optional[int] = None
    title: Optional[str] = None
