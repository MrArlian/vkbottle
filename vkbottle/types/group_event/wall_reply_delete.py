from typing import Optional

from ..base import VkObject


class WallReplyDelete(VkObject):
    owner_id: Optional[int] = None
    id: Optional[int] = None
    deleter_id: Optional[int] = None
    post_id: Optional[int] = None
