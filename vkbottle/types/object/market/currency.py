from __future__ import annotations

from ...base import VkObject


class Currency(VkObject):
    """VK Object MarketCurrency

    id - Currency ID
    name - Currency sign
    title - Currency title
    """

    id: int
    name: str
    title: str
