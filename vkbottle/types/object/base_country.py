from __future__ import annotations

from ..base import VkObject


class BaseCountry(VkObject):
    """VK Object BaseCountry

    id - Country ID
    title - Country title
    """

    id: int
    title: str
