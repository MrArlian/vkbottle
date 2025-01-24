from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .push_conversations import PushConversations
    from .push_params import PushParams


class PushSettings(VkObject):
    """VK Object AccountPushSettings

    conversations -
    disabled - Information whether notifications are disabled
    disabled_until - Time until that notifications are disabled in Unixtime
    settings -
    """

    conversations: Optional[PushConversations] = None
    disabled: Optional[bool] = None
    disabled_until: Optional[int] = None
    settings: Optional[PushParams] = None


AccountSubscriptions = List[int]
