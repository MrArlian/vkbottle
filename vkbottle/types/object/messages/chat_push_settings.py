from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ChatPushSettings(VkObject):
    """VK Object MessagesChatPushSettings

    disabled_until - Time until that notifications are disabled
    sound - Information whether the sound is on
    """

    disabled_until: Optional[int] = None
    sound: Optional[bool] = None
