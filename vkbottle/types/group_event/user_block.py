from typing import Optional

from ..base import VkObject


class UserBlock(VkObject):
    admin_id: int
    comment: Optional[str] = None
    reason: int
    unblock_date: int
    user_id: int
