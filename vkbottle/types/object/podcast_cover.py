from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .photos.photo_sizes import PhotoSizes


class PodcastCover(VkObject):
    """VK Object PodcastCover"""

    sizes: Optional[List[PhotoSizes]] = None
