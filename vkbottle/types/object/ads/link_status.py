from __future__ import annotations

from ...base import VkObject


class LinkStatus(VkObject):
    """VK Object AdsLinkStatus

    description - Reject reason
    redirect_url - URL
    status - Link status
    """

    description: str
    redirect_url: str
    status: str
