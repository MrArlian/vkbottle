from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .chat_settings_photo import ChatSettingsPhoto
    from ..base_link_button import BaseLinkButton


class ChatPreview(VkObject):
    """VK Object MessagesChatPreview"""

    admin_id: Optional[int] = None
    button: Optional[BaseLinkButton] = None
    is_don: Optional[bool] = None
    is_group_channel: Optional[bool] = None
    is_member: Optional[bool] = None
    joined: Optional[bool] = None
    local_id: Optional[int] = None
    members: Optional[List[int]] = None
    members_count: Optional[int] = None
    photo: Optional[ChatSettingsPhoto] = None
    title: Optional[str] = None
