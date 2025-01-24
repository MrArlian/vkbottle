from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import ButtonColor

from ...base import VkObject

from .keyboard_button_action_location import KeyboardButtonActionLocation
from .keyboard_button_action_open_app import KeyboardButtonActionOpenApp
from .keyboard_button_action_open_link import KeyboardButtonActionOpenLink
from .keyboard_button_action_open_photo import KeyboardButtonActionOpenPhoto
from .keyboard_button_action_text import KeyboardButtonActionText
from .keyboard_button_action_callback import KeyboardButtonActionCallback
from .keyboard_button_action_vkpay import KeyboardButtonActionVkpay


class KeyboardButtonPropertyAction(
    KeyboardButtonActionLocation,
    KeyboardButtonActionOpenApp,
    KeyboardButtonActionOpenLink,
    KeyboardButtonActionOpenPhoto,
    KeyboardButtonActionText,
    KeyboardButtonActionCallback,
    KeyboardButtonActionVkpay
):
    """
        VK Object MessagesKeyboardButtonPropertyAction
    """


class KeyboardButton(VkObject):
    """VK Object MessagesKeyboardButton

    action -
    color - Button color
    """

    action: KeyboardButtonPropertyAction
    color: Optional[ButtonColor] = None
