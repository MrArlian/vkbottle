from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseUserId(VkObject):
    """VK Object BaseUserId

    user_id - User ID
    """

    user_id: Optional[int] = None
