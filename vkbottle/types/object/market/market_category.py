from __future__ import annotations

from typing import TYPE_CHECKING

from ...base import VkObject

if TYPE_CHECKING:
    from .section import Section


class MarketCategory(VkObject):
    """VK Object MarketMarketCategoryOld

    id - Category ID
    name - Category name
    section -
    """

    id: int
    name: str
    section: Section
