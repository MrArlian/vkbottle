from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ItemPromoButtonAction(VkObject):
    """VK Object NewsfeedItemPromoButtonAction"""

    target: Optional[str] = None
    type: Optional[str] = None
    url: Optional[str] = None
