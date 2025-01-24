from ..base import VkObject


class MessageAllow(VkObject):
    key: str
    user_id: int
