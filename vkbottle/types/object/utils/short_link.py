from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ShortLink(VkObject):
    """VK Object UtilsShortLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    url - Full URL
    """

    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    url: Optional[str] = None
