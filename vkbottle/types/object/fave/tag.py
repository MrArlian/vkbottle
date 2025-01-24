from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Tag(VkObject):
    """VK Object FaveTag

    id - Tag id
    name - Tag name
    """

    id: Optional[int] = None
    name: Optional[str] = None
