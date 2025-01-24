from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PostedPhoto(VkObject):
    """VK Object WallPostedPhoto

    id - Photo ID
    owner_id - Photo owner's ID
    photo_130 - URL of the preview image with 130 px in width
    photo_604 - URL of the preview image with 604 px in width
    """

    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_130: Optional[str] = None
    photo_604: Optional[str] = None
