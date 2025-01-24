from __future__ import annotations

from typing import List, Optional

from vkbottle.enum.vk_object import (
    AccountPushParamsMode,
    AccountPushParamsOnoff,
    AccountPushParamsSettings
)

from ...base import VkObject


class PushParams(VkObject):
    """VK Object AccountPushParams"""

    app_request: Optional[List[AccountPushParamsOnoff]] = None
    birthday: Optional[List[AccountPushParamsOnoff]] = None
    chat: Optional[List[AccountPushParamsMode]] = None
    comment: Optional[List[AccountPushParamsSettings]] = None
    event_soon: Optional[List[AccountPushParamsOnoff]] = None
    friend: Optional[List[AccountPushParamsOnoff]] = None
    friend_accepted: Optional[List[AccountPushParamsOnoff]] = None
    friend_found: Optional[List[AccountPushParamsOnoff]] = None
    group_accepted: Optional[List[AccountPushParamsOnoff]] = None
    group_invite: Optional[List[AccountPushParamsOnoff]] = None
    like: Optional[List[AccountPushParamsSettings]] = None
    mention: Optional[List[AccountPushParamsSettings]] = None
    msg: Optional[List[AccountPushParamsMode]] = None
    new_post: Optional[List[AccountPushParamsOnoff]] = None
    reply: Optional[List[AccountPushParamsOnoff]] = None
    repost: Optional[List[AccountPushParamsSettings]] = None
    sdk_open: Optional[List[AccountPushParamsOnoff]] = None
    wall_post: Optional[List[AccountPushParamsOnoff]] = None
    wall_publish: Optional[List[AccountPushParamsOnoff]] = None
