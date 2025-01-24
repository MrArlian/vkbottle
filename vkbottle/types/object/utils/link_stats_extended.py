from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .stats_extended import StatsExtended


class LinkStatsExtended(VkObject):
    """VK Object UtilsLinkStatsExtended

    key - Link key (characters after vk.cc/)
    stats -
    """

    key: Optional[str] = None
    stats: Optional[List[StatsExtended]] = None
