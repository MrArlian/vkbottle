from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class LiveCovers(VkObject):
    """VK Object GroupsLiveCovers

    is_enabled - Information whether live covers is enabled
    is_scalable - Information whether live covers photo scaling is enabled
    story_ids -
    """

    is_enabled: bool
    is_scalable: Optional[bool] = None
    story_ids: Optional[List[str]] = None
