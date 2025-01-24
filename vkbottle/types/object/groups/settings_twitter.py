from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import GroupsSettingsTwitterStatus

from ...base import VkObject


class SettingsTwitter(VkObject):
    """VK Object GroupsSettingsTwitter"""

    name: Optional[str] = None
    status: GroupsSettingsTwitterStatus
