from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import PagesPrivacySettings

from ...base import VkObject


class WikipageFull(VkObject):
    """VK Object PagesWikipageFull

    created - Date when the page has been created in Unixtime
    creator_id - Page creator ID
    current_user_can_edit - Information whether current user can edit the page
    current_user_can_edit_access - Information whether current user can edit the page access settings
    edited - Date when the page has been edited in Unixtime
    editor_id - Last editor ID
    group_id - Community ID
    html - Page content, HTML
    id - Page ID
    owner_id - Owner ID
    parent - Parent
    parent2 - Parent2
    source - Page content, wiki
    title - Page title
    url - URL
    view_url - URL of the page preview
    views - Views number
    who_can_edit - Edit settings of the page
    who_can_view - View settings of the page
    """

    created: int
    creator_id: Optional[int] = None
    current_user_can_edit: Optional[bool] = None
    current_user_can_edit_access: Optional[bool] = None
    edited: int
    editor_id: Optional[int] = None
    group_id: int
    html: Optional[str] = None
    id: int
    owner_id: Optional[int] = None
    parent: Optional[str] = None
    parent2: Optional[str] = None
    source: Optional[str] = None
    title: str
    url: Optional[str] = None
    view_url: str
    views: int
    who_can_edit: PagesPrivacySettings
    who_can_view: PagesPrivacySettings
