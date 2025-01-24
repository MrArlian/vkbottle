from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LastShortenedLink(VkObject):
    """VK Object UtilsLastShortenedLink

    access_key - Access key for private stats
    key - Link key (characters after vk.cc/)
    short_url - Short link URL
    timestamp - Creation time in Unixtime
    url - Full URL
    views - Total views number
    """

    access_key: Optional[str] = None
    key: Optional[str] = None
    short_url: Optional[str] = None
    timestamp: Optional[int] = None
    url: Optional[str] = None
    views: Optional[int] = None
