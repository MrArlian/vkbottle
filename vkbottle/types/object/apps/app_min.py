from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AppsAppType

from ...base import VkObject


class AppMin(VkObject):
    """VK Object AppsAppMin

    author_owner_id - Application author's ID
    background_loader_color - Hex color code without hash sign
    icon_139 - URL of the app icon with 139 px in width
    icon_150 - URL of the app icon with 150 px in width
    icon_278 - URL of the app icon with 278 px in width
    icon_576 - URL of the app icon with 576 px in width
    icon_75 - URL of the app icon with 75 px in width
    id - Application ID
    is_installed - Is application installed
    loader_icon - SVG data
    title - Application title
    type -
    """

    author_owner_id: Optional[int] = None
    background_loader_color: Optional[str] = None
    icon_139: Optional[str] = None
    icon_150: Optional[str] = None
    icon_278: Optional[str] = None
    icon_576: Optional[str] = None
    icon_75: Optional[str] = None
    id: int
    is_installed: Optional[bool] = None
    loader_icon: Optional[str] = None
    title: str
    type: AppsAppType
