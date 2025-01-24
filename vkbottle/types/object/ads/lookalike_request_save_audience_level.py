from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LookalikeRequestSaveAudienceLevel(VkObject):
    """VK Object AdsLookalikeRequestSaveAudienceLevel

    audience_count - Saved audience audience size for according level
    level - Save audience level id, which is used in save audience queries
    """

    audience_count: Optional[int] = None
    level: Optional[int] = None
