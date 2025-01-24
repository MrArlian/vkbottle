from ..base import VkObject


class BoardPostDelete(VkObject):
    id: int
    topic_id: int
    topic_owner_id: int
