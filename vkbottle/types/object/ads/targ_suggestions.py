from __future__ import annotations

from typing import Optional

from ...base import VkObject


class TargSuggestions(VkObject):
    """VK Object AdsTargSuggestions

    id - Object ID
    name - Object name
    """

    id: Optional[int] = None
    name: Optional[str] = None
