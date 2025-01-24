from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import NewsfeedItemWallpostFeedbackType

from ...base import VkObject

if TYPE_CHECKING:
    from .item_wallpost_feedback_answer import ItemWallpostFeedbackAnswer


class ItemWallpostFeedback(VkObject):
    """VK Object NewsfeedItemWallpostFeedback"""

    answers: Optional[List[ItemWallpostFeedbackAnswer]] = None
    gratitude: Optional[str] = None
    question: str
    stars_count: Optional[int] = None
    type: NewsfeedItemWallpostFeedbackType
