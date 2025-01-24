from ..base import VkObject


class MessageTypingState(VkObject):
    state: str
    from_id: int
    to_id: int
