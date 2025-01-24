from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import (
    MessagesChatSettingsPermissionsChangeInfo,
    MessagesChatSettingsPermissionsChangePin,
    WhoCanMakeCalls,
    MessagesChatSettingsPermissionsUseMassMentions,
    WhoCanChangeAdmins,
    MessagesChatSettingsPermissionsSeeInviteLink,
    MessagesChatSettingsPermissionsInvite
)

from ...base import VkObject


class ChatSettingsPermissions(VkObject):
    """VK Object MessagesChatSettingsPermissions

    call - Who can make calls
    change_admins - Who can change admins
    change_info - Who can change chat info
    change_pin - Who can change pinned message
    invite - Who can invite users to chat
    see_invite_link - Who can see invite link
    use_mass_mentions - Who can use mass mentions
    """

    call: Optional[WhoCanMakeCalls] = None
    change_admins: Optional[WhoCanChangeAdmins] = None
    change_info: Optional[MessagesChatSettingsPermissionsChangeInfo] = None
    change_pin: Optional[MessagesChatSettingsPermissionsChangePin] = None
    invite: Optional[MessagesChatSettingsPermissionsInvite] = None
    see_invite_link: Optional[MessagesChatSettingsPermissionsSeeInviteLink] = None
    use_mass_mentions: Optional[MessagesChatSettingsPermissionsUseMassMentions] = None
