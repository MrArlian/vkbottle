from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .wallpost_comments_donut_placeholder import WallpostCommentsDonutPlaceholder


class WallpostCommentsDonut(VkObject):
    """VK Object WallWallpostCommentsDonut"""

    placeholder: Optional[WallpostCommentsDonutPlaceholder] = None
