from typing import Any, Optional

from vkbottle.enum.vk_object import (
    GroupsGroupIsClosed,
    GroupsGroupFullAgeLimits,
    GroupsGroupAudio,
    CallbackGroupMarket,
    GroupsGroupPhotos,
    GroupsGroupWall,
    GroupsGroupVideo
)

from ..base import VkObject


class GroupSettingsChanges(VkObject):
    access: Optional[GroupsGroupIsClosed] = None
    age_limits: Optional[GroupsGroupFullAgeLimits] = None
    description: Optional[str] = None
    enable_audio: Optional[GroupsGroupAudio] = None
    enable_market: Optional[CallbackGroupMarket] = None
    enable_photo: Optional[GroupsGroupPhotos] = None
    enable_status_default: Optional[GroupsGroupWall] = None
    enable_video: Optional[GroupsGroupVideo] = None
    public_category: Optional[int] = None
    public_subcategory: Optional[int] = None
    screen_name: Optional[str] = None
    title: Optional[str] = None
    website: Optional[str] = None
    old_value: Any
    new_value: Any
