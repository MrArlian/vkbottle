from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PostCopyright(VkObject):
    """VK Object WallPostCopyright"""

    id: Optional[int] = None
    link: str
    name: str
    type: str
