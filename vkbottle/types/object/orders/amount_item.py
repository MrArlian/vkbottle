from __future__ import annotations

from typing import Optional

from ...base import VkObject


class AmountItem(VkObject):
    """VK Object OrdersAmountItem

    amount - Votes amount in user's currency
    description - Amount description
    votes - Votes number
    """

    amount: Optional[float] = None
    description: Optional[str] = None
    votes: Optional[str] = None
