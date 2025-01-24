from typing import Optional

from ..base import VkObject


class VkpayTransaction(VkObject):
    amount: Optional[int] = None
    date: Optional[int] = None
    description: Optional[str] = None
    from_id: Optional[int] = None
