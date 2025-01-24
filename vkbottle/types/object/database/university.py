from __future__ import annotations

from typing import Optional

from ...base import VkObject


class University(VkObject):
    """VK Object DatabaseUniversity

    id - University ID
    title - University title
    """

    id: Optional[int] = None
    title: Optional[str] = None
