from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseImage(VkObject):
    """VK Object BaseImage

    height - Image height
    id -
    url - Image url
    width - Image width
    """

    height: int
    id: Optional[str] = None
    url: str
    width: int
