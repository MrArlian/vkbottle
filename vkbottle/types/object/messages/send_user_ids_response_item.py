from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_message_error import BaseMessageError


class SendUserIdsResponseItem(VkObject):
    """VK Object MessagesSendUserIdsResponseItem"""

    conversation_message_id: Optional[int] = None
    error: Optional[BaseMessageError] = None
    message_id: int
    peer_id: int
