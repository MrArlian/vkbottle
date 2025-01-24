from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Exports(VkObject):
    """VK Object UsersExports"""

    facebook: Optional[int] = None
    livejournal: Optional[int] = None
    twitter: Optional[int] = None
