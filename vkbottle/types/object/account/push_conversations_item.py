from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PushConversationsItem(VkObject):
    """VK Object AccountPushConversationsItem

    disabled_mass_mentions - Information whether the mass mentions (like '@all', '@online') are disabled. Can be affected by 'disabled_mentions'
    disabled_mentions - Information whether the mentions are disabled
    disabled_until - Time until that notifications are disabled in seconds
    peer_id - Peer ID
    sound - Information whether the sound are enabled
    """

    disabled_mass_mentions: Optional[bool] = None
    disabled_mentions: Optional[bool] = None
    disabled_until: int
    peer_id: int
    sound: bool
