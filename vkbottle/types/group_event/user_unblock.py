from ..base import VkObject


class UserUnblock(VkObject):
    admin_id: int
    by_end_date: int
    user_id: int
