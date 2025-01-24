from __future__ import annotations

from typing import List, Optional

from vkbottle.enum.vk_object import AdsAccessRolePublic

from ...base import VkObject


class UserSpecification(VkObject):
    """VK Object AdsUserSpecification"""

    client_ids: Optional[List[int]] = None
    grant_access_to_all_clients: Optional[bool] = None
    role: AdsAccessRolePublic
    user_id: int
    view_budget: Optional[bool] = None
