from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import ScopeName

from ...base import VkObject


class Scope(VkObject):
    """VK Object AppsScope

    name - Scope name
    title - Scope title
    """

    name: ScopeName
    title: Optional[str] = None
