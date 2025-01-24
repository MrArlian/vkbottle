from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseLinkApplicationStore(VkObject):
    """VK Object BaseLinkApplicationStore

    id - Store Id
    name - Store name
    """

    id: Optional[float] = None
    name: Optional[str] = None
