from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import FriendsFriendStatusStatus, BaseSex

from .user_min import UserMin

if TYPE_CHECKING:
    from ..friends.requests_mutual import RequestsMutual
    from .online_info import OnlineInfo


class User(UserMin):
    """VK Object UsersUser

    friend_status -
    mutual -
    online - Information whether the user is online
    online_app - Application ID
    online_info -
    online_mobile - Information whether the user is online in mobile site or application
    photo_100 - URL of square photo of the user with 100 pixels in width
    photo_50 - URL of square photo of the user with 50 pixels in width
    screen_name - Domain name of the user's page
    sex - User sex
    trending - Information whether the user has a "fire" pictogram.
    verified - Information whether the user is verified
    """

    friend_status: Optional[FriendsFriendStatusStatus] = None
    mutual: Optional[RequestsMutual] = None
    online: Optional[bool] = None
    online_app: Optional[int] = None
    online_info: Optional[OnlineInfo] = None
    online_mobile: Optional[bool] = None
    photo_100: Optional[str] = None
    photo_50: Optional[str] = None
    screen_name: Optional[str] = None
    sex: Optional[BaseSex] = None
    trending: Optional[bool] = None
    verified: Optional[bool] = None
