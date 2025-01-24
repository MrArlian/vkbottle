from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import StoriesStoryStatsState

from ...base import VkObject


class StoryStatsStat(VkObject):
    """VK Object StoriesStoryStatsStat

    count - Stat value
    state -
    """

    count: Optional[int] = None
    state: StoriesStoryStatsState
