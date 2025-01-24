from typing import Optional

from ..base import VkObject


class DonutSubscriptionCreate(VkObject):
    amount: int
    amount_without_fee: float
    user_id: Optional[int] = None
