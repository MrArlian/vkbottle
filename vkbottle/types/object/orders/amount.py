from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .amount_item import AmountItem


class Amount(VkObject):
    """VK Object OrdersAmount

    amounts -
    currency - Currency name
    """

    amounts: Optional[List[AmountItem]] = None
    currency: Optional[str] = None
