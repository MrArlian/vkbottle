from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import WallWallpostDonutEditMode

from ...base import VkObject

if TYPE_CHECKING:
    from .wallpost_donut_placeholder import WallpostDonutPlaceholder


class WallpostDonut(VkObject):
    """VK Object WallWallpostDonut

    can_publish_free_copy - Says whether group admin can post free copy of this donut post
    edit_mode - Says what user can edit in post about donut properties
    is_donut - Post only for dons
    paid_duration - Value of this field need to pass in wall.post/edit in donut_paid_duration
    placeholder - If placeholder was respond, text and all attachments will be hidden
    """

    can_publish_free_copy: Optional[bool] = None
    edit_mode: Optional[WallWallpostDonutEditMode] = None
    is_donut: bool
    paid_duration: Optional[int] = None
    placeholder: Optional[WallpostDonutPlaceholder] = None
