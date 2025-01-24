from __future__ import annotations

from vkbottle.enum.vk_object import MessagesKeyboardButtonActionOpenPhotoType

from ...base import VkObject


class KeyboardButtonActionOpenPhoto(VkObject):
    """VK Object MessagesKeyboardButtonActionOpenPhoto"""

    type: MessagesKeyboardButtonActionOpenPhotoType
