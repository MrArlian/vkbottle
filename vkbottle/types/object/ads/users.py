from __future__ import annotations

from typing import TYPE_CHECKING, List

from ...base import VkObject

if TYPE_CHECKING:
    from .accesses import Accesses


class Users(VkObject):
    """VK Object AdsUsers

    accesses -
    user_id - User ID
    """

    accesses: List[Accesses]
    user_id: int
