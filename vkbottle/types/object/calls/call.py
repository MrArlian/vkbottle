from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import CallsEndState

from ...base import VkObject

if TYPE_CHECKING:
    from .participants import Participants


class Call(VkObject):
    """VK Object CallsCall

    duration - Call duration
    initiator_id - Caller initiator
    participants -
    receiver_id - Caller receiver
    state -
    time - Timestamp for call
    video - Was this call initiated as video call
    """

    duration: Optional[int] = None
    initiator_id: int
    participants: Optional[Participants] = None
    receiver_id: int
    state: CallsEndState
    time: int
    video: Optional[bool] = None
