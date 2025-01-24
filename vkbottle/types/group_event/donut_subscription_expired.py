from typing import Optional

from ..base import VkObject


class DonutSubscriptionExpired(VkObject):
    user_id: Optional[int] = None
