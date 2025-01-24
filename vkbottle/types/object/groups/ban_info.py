from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import GroupsBanInfoReason

from ...base import VkObject


class BanInfo(VkObject):
    """VK Object GroupsBanInfo

    admin_id - Administrator ID
    comment - Comment for a ban
    comment_visible - Show comment for user
    date - Date when user has been added to blacklist in Unixtime
    end_date - Date when user will be removed from blacklist in Unixtime
    is_closed -
    reason -
    """

    admin_id: Optional[int] = None
    comment: Optional[str] = None
    comment_visible: Optional[bool] = None
    date: Optional[int] = None
    end_date: Optional[int] = None
    is_closed: Optional[bool] = None
    reason: Optional[GroupsBanInfoReason] = None
