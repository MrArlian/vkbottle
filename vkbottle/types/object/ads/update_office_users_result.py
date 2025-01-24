from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_error import BaseError


class UpdateOfficeUsersResult(VkObject):
    """VK Object AdsUpdateOfficeUsersResult"""

    error: Optional[BaseError] = None
    is_success: bool
    user_id: int
