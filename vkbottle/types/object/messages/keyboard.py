from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .keyboard_button import KeyboardButton


class Keyboard(VkObject):
    """VK Object MessagesKeyboard

    author_id - Community or bot, which set this keyboard
    buttons -
    inline -
    one_time - Should this keyboard disappear on first use
    """

    author_id: Optional[int] = None
    buttons: List[List[KeyboardButton]]
    inline: Optional[bool] = None
    one_time: bool
