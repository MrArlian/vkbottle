from __future__ import annotations

from typing import TYPE_CHECKING, List

from ..base import VkObject

if TYPE_CHECKING:
    from .base_image import BaseImage


class AppWidgetsPhoto(VkObject):
    """VK Object AppWidgetsPhoto

    id - Image ID
    images -
    """

    id: str
    images: List[BaseImage]
