from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .app_widgets_photo import AppWidgetsPhoto


class AppWidgetsPhotos(VkObject):
    """VK Object AppWidgetsPhotos"""

    count: Optional[int] = None
    items: Optional[List[AppWidgetsPhoto]] = None
