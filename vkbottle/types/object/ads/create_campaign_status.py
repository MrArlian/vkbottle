from __future__ import annotations

from typing import Optional

from ...base import VkObject


class CreateCampaignStatus(VkObject):
    """VK Object AdsCreateCampaignStatus

    error_code - Error code
    error_desc - Error description
    id - Campaign ID
    """

    error_code: Optional[int] = None
    error_desc: Optional[str] = None
    id: int
