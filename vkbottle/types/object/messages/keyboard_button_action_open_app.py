from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import MessagesKeyboardButtonActionOpenAppType

from ...base import VkObject


class KeyboardButtonActionOpenApp(VkObject):
    """VK Object MessagesKeyboardButtonActionOpenApp

    app_id - Fragment value in app link like vk.com/app{app_id}_-654321#hash
    hash - Fragment value in app link like vk.com/app123456_-654321#{hash}
    label - Label for button
    owner_id - Fragment value in app link like vk.com/app123456_{owner_id}#hash
    payload - Additional data sent along with message for developer convenience
    type -
    """

    app_id: int
    hash: Optional[str] = None
    label: str
    owner_id: int
    payload: Optional[str] = None
    type: MessagesKeyboardButtonActionOpenAppType
