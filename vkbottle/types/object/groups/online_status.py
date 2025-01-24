from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import GroupsOnlineStatusType

from ...base import VkObject


class OnlineStatus(VkObject):
    """VK Object GroupsOnlineStatus

    minutes - Estimated time of answer (for status = answer_mark)
    status -
    """

    minutes: Optional[int] = None
    status: GroupsOnlineStatusType
