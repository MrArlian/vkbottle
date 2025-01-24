from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import GroupsOwnerXtrBanInfoType

from ...base import VkObject

if TYPE_CHECKING:
    from .ban_info import BanInfo
    from .group import Group
    from ..users.user import User


class OwnerXtrBanInfo(VkObject):
    """VK Object GroupsOwnerXtrBanInfo

    ban_info -
    group - Information about group if type = group
    profile - Information about group if type = profile
    type -
    """

    ban_info: Optional[BanInfo] = None
    group: Optional[Group] = None
    profile: Optional[User] = None
    type: Optional[GroupsOwnerXtrBanInfoType] = None
