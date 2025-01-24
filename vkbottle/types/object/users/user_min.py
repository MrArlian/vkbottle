from __future__ import annotations

from typing import Optional

from ...base import VkObject


class UserMin(VkObject):
    """VK Object UsersUserMin

    can_access_closed -
    deactivated - Returns if a profile is deleted or blocked
    first_name - User first name
    hidden - Returns if a profile is hidden.
    id - User ID
    is_closed -
    last_name - User last name
    """

    can_access_closed: Optional[bool] = None
    deactivated: Optional[str] = None
    first_name: Optional[str] = None
    hidden: Optional[int] = None
    id: int
    is_closed: Optional[bool] = None
    last_name: Optional[str] = None
