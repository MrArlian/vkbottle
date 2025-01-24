from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Graffiti(VkObject):
    """VK Object WallGraffiti

    access_key - Access key for graffiti
    height - Graffiti height
    id - Graffiti ID
    owner_id - Graffiti owner's ID
    photo_200 - URL of the preview image with 200 px in width
    photo_586 - URL of the preview image with 586 px in width
    url - Graffiti URL
    width - Graffiti width
    """

    access_key: Optional[str] = None
    height: Optional[int] = None
    id: Optional[int] = None
    owner_id: Optional[int] = None
    photo_200: Optional[str] = None
    photo_586: Optional[str] = None
    url: Optional[str] = None
    width: Optional[int] = None
