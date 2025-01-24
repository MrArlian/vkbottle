from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .app import App
    from ..users.user_min import UserMin


class CatalogList(VkObject):
    """VK Object AppsCatalogList

    count - Total number
    items -
    profiles -
    """

    count: int
    items: List[App]
    profiles: Optional[List[UserMin]] = None
