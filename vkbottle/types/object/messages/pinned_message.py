from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_geo import BaseGeo
    from .foreign_message import ForeignMessage
    from .message_attachment import MessageAttachment
    from .keyboard import Keyboard


class PinnedMessage(VkObject):
    """VK Object MessagesPinnedMessage

    attachments -
    conversation_message_id - Unique auto-incremented number for all messages with this peer
    date - Date when the message has been sent in Unixtime
    from_id - Message author's ID
    fwd_messages - Forwarded messages
    geo -
    id - Message ID
    keyboard -
    peer_id - Peer ID
    reply_message -
    text - Message text
    """

    attachments: Optional[List[MessageAttachment]] = None
    conversation_message_id: Optional[int] = None
    date: int
    from_id: int
    fwd_messages: Optional[List[ForeignMessage]] = None
    geo: Optional[BaseGeo] = None
    id: int
    keyboard: Optional[Keyboard] = None
    peer_id: int
    reply_message: Optional[ForeignMessage] = None
    text: str
