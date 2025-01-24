from __future__ import annotations

from typing import Optional

from ...base import VkObject


class TargetGroup(VkObject):
    """VK Object AdsTargetGroup

    audience_count - Audience
    domain - Site domain
    id - Group ID
    lifetime - Number of days for user to be in group
    name - Group name
    pixel - Pixel code
    """

    audience_count: Optional[int] = None
    domain: Optional[str] = None
    id: Optional[int] = None
    lifetime: Optional[int] = None
    name: Optional[str] = None
    pixel: Optional[str] = None
