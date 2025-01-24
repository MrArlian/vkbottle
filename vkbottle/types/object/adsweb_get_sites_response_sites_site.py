from __future__ import annotations

from typing import Optional

from ..base import VkObject


class AdswebGetSitesResponseSitesSite(VkObject):
    """VK Object AdswebGetSitesResponseSitesSite"""

    domains: Optional[str] = None
    id: int
    status_moder: Optional[str] = None
    status_user: Optional[str] = None
