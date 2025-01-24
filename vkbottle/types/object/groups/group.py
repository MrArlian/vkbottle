from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import GroupsGroupAdminLevel, GroupsGroupIsClosed, GroupsGroupType

from ...base import VkObject

if TYPE_CHECKING:
    from ..video.live_info import LiveInfo
    from .photo_size import PhotoSize


class Group(VkObject):
    """VK Object GroupsGroup

    admin_level -
    deactivated - Information whether community is banned
    est_date - Established date
    finish_date - Finish date in Unixtime format
    id - Community ID
    is_admin - Information whether current user is administrator
    is_advertiser - Information whether current user is advertiser
    is_closed -
    is_member - Information whether current user is member
    is_video_live_notifications_blocked -
    name - Community name
    photo_100 - URL of square photo of the community with 100 pixels in width
    photo_200 - URL of square photo of the community with 200 pixels in width
    photo_200_orig - URL of square photo of the community with 200 pixels in width original
    photo_400 - URL of square photo of the community with 400 pixels in width
    photo_400_orig - URL of square photo of the community with 400 pixels in width original
    photo_50 - URL of square photo of the community with 50 pixels in width
    photo_max - URL of square photo of the community with max pixels in width
    photo_max_orig - URL of square photo of the community with max pixels in width original
    photo_max_size -
    public_date_label - Public date label
    screen_name - Domain of the community page
    start_date - Start date in Unixtime format
    type -
    video_live -
    """

    admin_level: Optional[GroupsGroupAdminLevel] = None
    deactivated: Optional[str] = None
    est_date: Optional[str] = None
    finish_date: Optional[int] = None
    id: int
    is_admin: Optional[bool] = None
    is_advertiser: Optional[bool] = None
    is_closed: Optional[GroupsGroupIsClosed] = None
    is_member: Optional[bool] = None
    is_video_live_notifications_blocked: Optional[bool] = None
    name: Optional[str] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_200_orig: Optional[str] = None
    photo_400: Optional[str] = None
    photo_400_orig: Optional[str] = None
    photo_50: Optional[str] = None
    photo_max: Optional[str] = None
    photo_max_orig: Optional[str] = None
    photo_max_size: Optional[PhotoSize] = None
    public_date_label: Optional[str] = None
    screen_name: Optional[str] = None
    start_date: Optional[int] = None
    type: Optional[GroupsGroupType] = None
    video_live: Optional[LiveInfo] = None
