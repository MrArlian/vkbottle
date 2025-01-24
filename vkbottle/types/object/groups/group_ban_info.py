from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import GroupsBanInfoReason

from ...base import VkObject


class GroupBanInfo(VkObject):
    """VK Object GroupsGroupBanInfo

    comment - Ban comment
    end_date - End date of ban in Unixtime
    reason -
    """

    comment: Optional[str] = None
    end_date: Optional[int] = None
    reason: Optional[GroupsBanInfoReason] = None
