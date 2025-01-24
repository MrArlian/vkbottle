from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_user_id import BaseUserId


class ItemFriendFriends(VkObject):
    """VK Object NewsfeedItemFriendFriends

    count - Number of friends has been added
    items -
    """

    count: Optional[int] = None
    items: Optional[List[BaseUserId]] = None
