from __future__ import annotations

from typing import TYPE_CHECKING

from ...base import VkObject

if TYPE_CHECKING:
    from .story_stats_stat import StoryStatsStat


class StoryStats(VkObject):
    """VK Object StoriesStoryStats"""

    answer: StoryStatsStat
    bans: StoryStatsStat
    likes: StoryStatsStat
    open_link: StoryStatsStat
    replies: StoryStatsStat
    shares: StoryStatsStat
    subscribers: StoryStatsStat
    views: StoryStatsStat
