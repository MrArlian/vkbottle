from __future__ import annotations

from typing import List, Optional

from vkbottle.enum.vk_object import MessagesTemplateActionTypeNames

from ..base import VkObject


class ClientInfoForBots(VkObject):
    """VK Object ClientInfoForBots

    button_actions -
    carousel - client has support carousel
    inline_keyboard - client has support inline keyboard
    keyboard - client has support keyboard
    lang_id - client or user language id
    """

    button_actions: Optional[List[MessagesTemplateActionTypeNames]] = None
    carousel: Optional[bool] = None
    inline_keyboard: Optional[bool] = None
    keyboard: Optional[bool] = None
    lang_id: Optional[int] = None
