from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Faculty(VkObject):
    """VK Object DatabaseFaculty

    id - Faculty ID
    title - Faculty title
    """

    id: Optional[int] = None
    title: Optional[str] = None
