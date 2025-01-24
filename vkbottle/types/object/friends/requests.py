from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .requests_mutual import RequestsMutual


class Requests(VkObject):
    """VK Object FriendsRequests

    _from - ID of the user by whom friend has been suggested
    mutual -
    user_id - User ID
    """

    _from: Optional[str] = None
    mutual: Optional[RequestsMutual] = None
    user_id: Optional[int] = None
