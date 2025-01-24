from __future__ import annotations

from typing import Optional

from ...base import VkObject


class SmsNotification(VkObject):
    """VK Object SecureSmsNotification

    app_id - Application ID
    date - Date when message has been sent in Unixtime
    id - Notification ID
    message - Messsage text
    user_id - User ID
    """

    app_id: Optional[str] = None
    date: Optional[str] = None
    id: Optional[str] = None
    message: Optional[str] = None
    user_id: Optional[str] = None
