from __future__ import annotations

from ...base import VkObject


class LastActivity(VkObject):
    """VK Object MessagesLastActivity

    online - Information whether user is online
    time - Time when user was online in Unixtime
    """

    online: bool
    time: int
