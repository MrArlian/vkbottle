from typing import Optional

from ..base import VkObject


class GroupLeave(VkObject):
    self: Optional[bool] = None
    user_id: Optional[int] = None
