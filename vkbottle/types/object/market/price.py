from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .currency import Currency


class Price(VkObject):
    """VK Object MarketPrice

    amount - Amount
    currency -
    discount_rate -
    old_amount -
    old_amount_text - Textual representation of old price
    text - Text
    """

    amount: str
    currency: Currency
    discount_rate: Optional[int] = None
    old_amount: Optional[str] = None
    old_amount_text: Optional[str] = None
    text: str
