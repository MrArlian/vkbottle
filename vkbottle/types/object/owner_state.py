from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import OwnerStateState

from ..base import VkObject


class OwnerState(VkObject):
    """VK Object OwnerState

    description - wiki text to describe user state
    state -
    """

    description: Optional[str] = None
    state: Optional[OwnerStateState] = None
