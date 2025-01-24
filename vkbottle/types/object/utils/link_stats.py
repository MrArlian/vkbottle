from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .stats import Stats


class LinkStats(VkObject):
    """VK Object UtilsLinkStats

    key - Link key (characters after vk.cc/)
    stats -
    """

    key: Optional[str] = None
    stats: Optional[List[Stats]] = None
