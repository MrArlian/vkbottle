from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import UsersOnlineInfoStatus

from ...base import VkObject


class OnlineInfo(VkObject):
    """VK Object UsersOnlineInfo

    app_id - Application id from which user is currently online or was last seen online
    is_mobile - Is user online from desktop app or mobile app
    is_online - Whether user is currently online or not
    last_seen - Last time we saw user being active
    status - In case user online is not visible, it indicates approximate timeframe of user online
    visible - Whether you can see real online status of user or not
    """

    app_id: Optional[int] = None
    is_mobile: Optional[bool] = None
    is_online: Optional[bool] = None
    last_seen: Optional[int] = None
    status: Optional[UsersOnlineInfoStatus] = None
    visible: bool
