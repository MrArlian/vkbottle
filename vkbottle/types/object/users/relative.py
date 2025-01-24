from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import RelativeType

from ...base import VkObject


class Relative(VkObject):
    """VK Object UsersRelative

    birth_date - Date of child birthday (format dd.mm.yyyy)
    id - Relative ID
    name - Name of relative
    type - Relative type
    """

    birth_date: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: RelativeType
