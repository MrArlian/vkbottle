from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import UsersUserType

from .user import User


class UserXtrType(User):
    """VK Object UsersUserXtrType"""

    type: Optional[UsersUserType] = None
