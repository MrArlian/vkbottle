from __future__ import annotations

from ...base import VkObject


class Client(VkObject):
    """VK Object AdsClient

    all_limit - Client's total limit, rubles
    day_limit - Client's day limit, rubles
    id - Client ID
    name - Client name
    """

    all_limit: str
    day_limit: str
    id: int
    name: str
