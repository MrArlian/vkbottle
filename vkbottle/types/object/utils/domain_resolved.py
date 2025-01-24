from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import UtilsDomainResolvedType

from ...base import VkObject


class DomainResolved(VkObject):
    """VK Object UtilsDomainResolved

    group_id - Group ID
    object_id - Object ID
    type -
    """

    group_id: Optional[int] = None
    object_id: Optional[int] = None
    type: Optional[UtilsDomainResolvedType] = None
