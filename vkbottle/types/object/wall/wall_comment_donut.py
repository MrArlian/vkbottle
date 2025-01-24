from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .wall_comment_donut_placeholder import WallCommentDonutPlaceholder


class WallCommentDonut(VkObject):
    """VK Object WallWallCommentDonut

    is_don - Means commentator is donator
    placeholder -
    """

    is_don: Optional[bool] = None
    placeholder: Optional[WallCommentDonutPlaceholder] = None
