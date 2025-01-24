from __future__ import annotations

from typing import Optional

from ...base import VkObject


class School(VkObject):
    """VK Object DatabaseSchool

    id - School ID
    title - School title
    """

    id: Optional[int] = None
    title: Optional[str] = None
