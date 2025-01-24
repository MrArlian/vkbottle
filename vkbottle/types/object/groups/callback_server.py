from __future__ import annotations

from vkbottle.enum.vk_object import GroupsCallbackServerStatus

from ...base import VkObject


class CallbackServer(VkObject):
    """VK Object GroupsCallbackServer"""

    creator_id: int
    id: int
    secret_key: str
    status: GroupsCallbackServerStatus
    title: str
    url: str
