from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .podcast_cover import PodcastCover


class PodcastExternalData(VkObject):
    """VK Object PodcastExternalData

    cover - Podcast cover
    owner_name - Name of the podcasts owner community
    owner_url - Url of the podcasts owner community
    title - Podcast title
    url - Url of the podcast page
    """

    cover: Optional[PodcastCover] = None
    owner_name: Optional[str] = None
    owner_url: Optional[str] = None
    title: Optional[str] = None
    url: Optional[str] = None
