from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import BaseLinkButtonActionType

from ..base import VkObject


class BaseLinkButtonAction(VkObject):
    """VK Object BaseLinkButtonAction

    consume_reason -
    type -
    url - Action URL
    """

    consume_reason: Optional[str] = None
    type: BaseLinkButtonActionType
    url: Optional[str] = None
