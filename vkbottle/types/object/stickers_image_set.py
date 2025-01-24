from __future__ import annotations

from typing import Optional

from ..base import VkObject


class StickersImageSet(VkObject):
    """VK Object StickersImageSet

    base_url - Base URL for images in set
    version - Version number to be appended to the image URL
    """

    base_url: str
    version: Optional[int] = None
