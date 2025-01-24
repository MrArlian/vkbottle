from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ChatSettingsAcl(VkObject):
    """VK Object MessagesChatSettingsAcl

    can_call - Can you init group call in the chat
    can_change_info - Can you change photo, description and name
    can_change_invite_link - Can you change invite link for this chat
    can_change_pin - Can you pin/unpin message for this chat
    can_change_service_type - Can you change chat service type
    can_copy_chat - Can you copy chat
    can_invite - Can you invite other peers in chat
    can_moderate - Can you moderate (delete) other users' messages
    can_promote_users - Can you promote simple users to chat admins
    can_see_invite_link - Can you see invite link for this chat
    can_use_mass_mentions - Can you use mass mentions
    """

    can_call: bool
    can_change_info: bool
    can_change_invite_link: bool
    can_change_pin: bool
    can_change_service_type: Optional[bool] = None
    can_copy_chat: bool
    can_invite: bool
    can_moderate: bool
    can_promote_users: bool
    can_see_invite_link: bool
    can_use_mass_mentions: bool
