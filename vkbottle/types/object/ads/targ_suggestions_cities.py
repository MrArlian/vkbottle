from __future__ import annotations

from typing import Optional

from ...base import VkObject


class TargSuggestionsCities(VkObject):
    """VK Object AdsTargSuggestionsCities

    id - Object ID
    name - Object name
    parent - Parent object
    """

    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None
