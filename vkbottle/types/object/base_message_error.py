from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseMessageError(VkObject):
    """VK Object BaseMessageError

    code - Error code
    description - Error message
    """

    code: Optional[int] = None
    description: Optional[str] = None
