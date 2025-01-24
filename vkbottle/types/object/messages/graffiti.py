from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Graffiti(VkObject):
    """VK Object MessagesGraffiti

    access_key - Access key for graffiti
    height - Graffiti height
    id - Graffiti ID
    owner_id - Graffiti owner ID
    url - Graffiti URL
    width - Graffiti width
    """

    access_key: Optional[str] = None
    height: int
    id: int
    owner_id: int
    url: str
    width: int
