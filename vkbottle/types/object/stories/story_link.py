from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StoryLink(VkObject):
    """VK Object StoriesStoryLink

    link_url_target - How to open url
    text - Link text
    url - Link URL
    """

    link_url_target: Optional[str] = None
    text: str
    url: str
