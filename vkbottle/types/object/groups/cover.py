from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_image import BaseImage


class Cover(VkObject):
    """VK Object GroupsCover

    enabled - Information whether cover is enabled
    images -
    """

    enabled: bool
    images: Optional[List[BaseImage]] = None
