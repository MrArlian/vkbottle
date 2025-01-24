from ..base import VkObject


class MarketCommentDelete(VkObject):
    id: int
    item_id: int
    owner_id: int
    user_id: int
    deleter_id: int
