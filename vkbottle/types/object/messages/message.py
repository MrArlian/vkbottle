from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from pydantic import Field

from ...base import VkObject

if TYPE_CHECKING:
    from .message_action import MessageAction
    from .keyboard import Keyboard
    from ..base_geo import BaseGeo
    from .message_attachment import MessageAttachment
    from .foreign_message import ForeignMessage


class Message(VkObject):
    """VK Object MessagesMessage

    action -
    admin_author_id - Only for messages from community. Contains user ID of community admin, who sent this message.
    attachments -
    conversation_message_id - Unique auto-incremented number for all messages with this peer
    date - Date when the message has been sent in Unixtime
    deleted - Is it an deleted message
    from_id - Message author's ID
    fwd_messages - Forwarded messages
    geo -
    id - Message ID
    important - Is it an important message
    is_cropped - this message is cropped for bot
    is_hidden -
    is_silent - Is silent message, push without sound
    keyboard -
    members_count - Members number
    out - Information whether the message is outcoming
    payload -
    peer_id - Peer ID
    pinned_at - Date when the message has been pinned in Unixtime
    random_id - ID used for sending messages. It returned only for outgoing messages
    ref -
    ref_source -
    reply_message -
    text - Message text
    update_time - Date when the message has been updated in Unixtime
    was_listened - Was the audio message inside already listened by you
    """

    action: Optional[MessageAction] = None
    admin_author_id: Optional[int] = None
    attachments: List[MessageAttachment] = Field(default_factory=list)
    conversation_message_id: Optional[int] = None
    date: int
    deleted: Optional[bool] = None
    from_id: int
    fwd_messages: Optional[List[ForeignMessage]] = None
    geo: Optional[BaseGeo] = None
    id: int
    important: Optional[bool] = None
    is_cropped: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_silent: Optional[bool] = None
    keyboard: Optional[Keyboard] = None
    members_count: Optional[int] = None
    out: bool
    payload: Optional[str] = None
    peer_id: int
    pinned_at: Optional[int] = None
    random_id: Optional[int] = None
    ref: Optional[str] = None
    ref_source: Optional[str] = None
    reply_message: Optional[ForeignMessage] = None
    text: str
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
