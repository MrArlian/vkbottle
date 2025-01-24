from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import MessagesKeyboardButtonActionLocationType

from ...base import VkObject


class KeyboardButtonActionLocation(VkObject):
    """VK Object MessagesKeyboardButtonActionLocation

    payload - Additional data sent along with message for developer convenience
    type -
    """

    payload: Optional[str] = None
    type: MessagesKeyboardButtonActionLocationType
