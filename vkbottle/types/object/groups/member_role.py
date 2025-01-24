from __future__ import annotations

from typing import List, Optional

from vkbottle.enum.vk_object import GroupsMemberRoleStatus, GroupsMemberRolePermission

from ...base import VkObject


class MemberRole(VkObject):
    """VK Object GroupsMemberRole

    id - User ID
    permissions -
    role -
    """

    id: int
    permissions: Optional[List[GroupsMemberRolePermission]] = None
    role: Optional[GroupsMemberRoleStatus] = None
