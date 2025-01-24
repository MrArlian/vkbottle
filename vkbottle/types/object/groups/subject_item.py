from __future__ import annotations

from ...base import VkObject


class SubjectItem(VkObject):
    """VK Object GroupsSubjectItem

    id - Subject ID
    name - Subject title
    """

    id: int
    name: str
