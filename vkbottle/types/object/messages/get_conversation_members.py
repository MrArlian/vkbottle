from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .conversation_member import ConversationMember
    from .chat_restrictions import ChatRestrictions
    from ..groups.group_full import GroupFull
    from ..users.user_full import UserFull


class GetConversationMembers(VkObject):
    """VK Object MessagesGetConversationMembers

    chat_restrictions -
    count - Chat members count
    groups -
    items -
    profiles -
    """

    chat_restrictions: Optional[ChatRestrictions] = None
    count: int
    groups: Optional[List[GroupFull]] = None
    items: List[ConversationMember]
    profiles: Optional[List[UserFull]] = None
