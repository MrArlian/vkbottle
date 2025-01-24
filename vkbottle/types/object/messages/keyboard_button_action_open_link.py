from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import MessagesKeyboardButtonActionOpenLinkType

from ...base import VkObject


class KeyboardButtonActionOpenLink(VkObject):
    """VK Object MessagesKeyboardButtonActionOpenLink

    label - Label for button
    link - link for button
    payload - Additional data sent along with message for developer convenience
    type -
    """

    label: str
    link: str
    payload: Optional[str] = None
    type: MessagesKeyboardButtonActionOpenLinkType
