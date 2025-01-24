from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import MessagesKeyboardButtonActionVkpayType

from ...base import VkObject


class KeyboardButtonActionVkpay(VkObject):
    """VK Object MessagesKeyboardButtonActionVkpay

    hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
    payload - Additional data sent along with message for developer convenience
    type -
    """

    hash: str
    payload: Optional[str] = None
    type: MessagesKeyboardButtonActionVkpayType
