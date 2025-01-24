from typing import Optional

from ..base import VkObject


class DonutSubscriptionPriceChanged(VkObject):
    amount_diff: Optional[float] = None
    amount_diff_without_fee: Optional[float] = None
    amount_new: int
    amount_old: int
    user_id: Optional[int] = None
