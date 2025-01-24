from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .feedback import Feedback
    from .reply import Reply
    from .notification import Notification


class Notification(VkObject):
    """VK Object NotificationsNotification

    date - Date when the event has been occurred
    feedback -
    parent -
    reply -
    type - Notification type
    """

    date: Optional[int] = None
    feedback: Optional[Feedback] = None
    parent: Optional[Notification] = None
    reply: Optional[Reply] = None
    type: Optional[str] = None
