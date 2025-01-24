from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseObjectCount(VkObject):
    """VK Object BaseObjectCount

    count - Items count
    """

    count: Optional[int] = None
