from __future__ import annotations

from typing import Optional

from ...base import VkObject


class CreateAdStatus(VkObject):
    """VK Object AdsCreateAdStatus

    error_code - Error code
    error_desc - Error description
    id - Ad ID
    post_id - Stealth Post ID
    """

    error_code: Optional[int] = None
    error_desc: Optional[str] = None
    id: int
    post_id: Optional[int] = None
