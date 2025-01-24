from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Occupation(VkObject):
    """VK Object UsersOccupation

    id - ID of school, university, company group
    name - Name of occupation
    type - Type of occupation
    """

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
