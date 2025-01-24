from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import PagesPrivacySettings

from ...base import VkObject


class Wikipage(VkObject):
    """VK Object PagesWikipage

    creator_id - Page creator ID
    creator_name - Page creator name
    editor_id - Last editor ID
    editor_name - Last editor name
    group_id - Community ID
    id - Page ID
    title - Page title
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

    creator_id: Optional[int] = None
    creator_name: Optional[str] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
    group_id: int
    id: int
    title: str
    views: int
    who_can_edit: PagesPrivacySettings
    who_can_view: PagesPrivacySettings
