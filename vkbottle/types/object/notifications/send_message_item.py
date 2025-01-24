from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .send_message_error import SendMessageError


class SendMessageItem(VkObject):
    """VK Object NotificationsSendMessageItem

    error -
    status - Notification status
    user_id - User ID
    """

    error: Optional[SendMessageError] = None
    status: Optional[bool] = None
    user_id: Optional[int] = None
