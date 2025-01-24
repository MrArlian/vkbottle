from typing import Optional

from ..base import VkObject


class DonutSubscriptionCancelled(VkObject):
    user_id: Optional[int] = None
