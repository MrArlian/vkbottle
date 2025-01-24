from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AdsAccessRolePublic

from ...base import VkObject


class UserSpecificationCutted(VkObject):
    """VK Object AdsUserSpecificationCutted"""

    client_id: Optional[int] = None
    role: AdsAccessRolePublic
    user_id: int
    view_budget: Optional[bool] = None
