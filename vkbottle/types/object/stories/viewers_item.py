from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..users.user_full import UserFull


class ViewersItem(VkObject):
    """VK Object StoriesViewersItem

    is_liked - user has like for this object
    user -
    user_id - user id
    """

    is_liked: bool
    user: Optional[UserFull] = None
    user_id: int
