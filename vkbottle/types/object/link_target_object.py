from __future__ import annotations

from typing import Optional

from ..base import VkObject


class LinkTargetObject(VkObject):
    """VK Object LinkTargetObject

    item_id - Item ID
    owner_id - Owner ID
    type - Object type
    """

    item_id: Optional[int] = None
    owner_id: Optional[int] = None
    type: Optional[str] = None
