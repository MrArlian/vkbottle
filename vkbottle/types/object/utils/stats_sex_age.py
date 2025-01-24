from __future__ import annotations

from typing import Optional

from ...base import VkObject


class StatsSexAge(VkObject):
    """VK Object UtilsStatsSexAge

    age_range - Age denotation
    female - Views by female users
    male - Views by male users
    """

    age_range: Optional[str] = None
    female: Optional[int] = None
    male: Optional[int] = None
