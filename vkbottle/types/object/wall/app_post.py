from __future__ import annotations

from typing import Optional

from ...base import VkObject


class AppPost(VkObject):
    """VK Object WallAppPost

    id - Application ID
    name - Application name
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: Optional[int] = None
    name: Optional[str] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None
