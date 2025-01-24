from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import ErrorCode

from ...base import VkObject


class SendMessageError(VkObject):
    """VK Object NotificationsSendMessageError

    code - Error code
    description - Error description
    """

    code: Optional[ErrorCode] = None
    description: Optional[str] = None
