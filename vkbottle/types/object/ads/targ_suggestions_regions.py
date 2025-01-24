from __future__ import annotations

from typing import Optional

from ...base import VkObject


class TargSuggestionsRegions(VkObject):
    """VK Object AdsTargSuggestionsRegions

    id - Object ID
    name - Object name
    type - Object type
    """

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
