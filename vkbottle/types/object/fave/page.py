from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import FavePageType

from ...base import VkObject

if TYPE_CHECKING:
    from .tag import Tag
    from ..groups.group_full import GroupFull
    from ..users.user_full import UserFull


class Page(VkObject):
    """VK Object FavePage

    description - Some info about user or group
    group -
    tags -
    type - Item type
    updated_date - Timestamp, when this page was bookmarked
    user -
    """

    description: str
    group: Optional[GroupFull] = None
    tags: List[Tag]
    type: FavePageType
    updated_date: Optional[int] = None
    user: Optional[UserFull] = None
