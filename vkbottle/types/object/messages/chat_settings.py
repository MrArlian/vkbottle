from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import MessagesChatSettingsState

from ...base import VkObject

if TYPE_CHECKING:
    from .chat_settings_photo import ChatSettingsPhoto
    from .chat_settings_permissions import ChatSettingsPermissions
    from .chat_settings_acl import ChatSettingsAcl
    from .pinned_message import PinnedMessage


class ChatSettings(VkObject):
    """VK Object MessagesChatSettings

    acl -
    active_ids -
    admin_ids - Ids of chat admins
    disappearing_chat_link -
    friends_count -
    is_disappearing -
    is_group_channel -
    is_service -
    members_count -
    owner_id -
    permissions -
    photo -
    pinned_message -
    state -
    theme -
    title - Chat title
    """

    acl: ChatSettingsAcl
    active_ids: List[int]
    admin_ids: Optional[List[int]] = None
    disappearing_chat_link: Optional[str] = None
    friends_count: Optional[int] = None
    is_disappearing: Optional[bool] = None
    is_group_channel: Optional[bool] = None
    is_service: Optional[bool] = None
    members_count: Optional[int] = None
    owner_id: int
    permissions: Optional[ChatSettingsPermissions] = None
    photo: Optional[ChatSettingsPhoto] = None
    pinned_message: Optional[PinnedMessage] = None
    state: MessagesChatSettingsState
    theme: Optional[str] = None
    title: str
