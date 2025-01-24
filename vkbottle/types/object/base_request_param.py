from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseRequestParam(VkObject):
    """VK Object BaseRequestParam

    key - Parameter name
    value - Parameter value
    """

    key: Optional[str] = None
    value: Optional[str] = None
