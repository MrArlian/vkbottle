from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ChatRestrictions(VkObject):
    """VK Object MessagesChatRestrictions

    admins_promote_users - Only admins can promote users to admins
    only_admins_edit_info - Only admins can change chat info
    only_admins_edit_pin - Only admins can edit pinned message
    only_admins_invite - Only admins can invite users to this chat
    only_admins_kick - Only admins can kick users from this chat
    """

    admins_promote_users: Optional[bool] = None
    only_admins_edit_info: Optional[bool] = None
    only_admins_edit_pin: Optional[bool] = None
    only_admins_invite: Optional[bool] = None
    only_admins_kick: Optional[bool] = None
