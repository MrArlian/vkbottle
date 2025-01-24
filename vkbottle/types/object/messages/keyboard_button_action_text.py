from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import MessagesKeyboardButtonActionTextType

from ...base import VkObject


class KeyboardButtonActionText(VkObject):
    """VK Object MessagesKeyboardButtonActionText

    label - Label for button
    payload - Additional data sent along with message for developer convenience
    type -
    """

    label: str
    payload: Optional[str] = None
    type: MessagesKeyboardButtonActionTextType
