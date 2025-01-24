from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_geo import BaseGeo
    from .foreign_message import ForeignMessage
    from .message_attachment import MessageAttachment


class ForeignMessage(VkObject):
    """VK Object MessagesForeignMessage

    attachments -
    conversation_message_id - Conversation message ID
    date - Date when the message was created
    from_id - Message author's ID
    fwd_messages -
    geo -
    id - Message ID
    payload - Additional data sent along with message for developer convenience
    peer_id - Peer ID
    reply_message -
    text - Message text
    update_time - Date when the message has been updated in Unixtime
    was_listened - Was the audio message inside already listened by you
    """

    attachments: Optional[List[MessageAttachment]] = None
    conversation_message_id: Optional[int] = None
    date: int
    from_id: int
    fwd_messages: Optional[List[ForeignMessage]] = None
    geo: Optional[BaseGeo] = None
    id: Optional[int] = None
    payload: Optional[str] = None
    peer_id: Optional[int] = None
    reply_message: Optional[ForeignMessage] = None
    text: str
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
