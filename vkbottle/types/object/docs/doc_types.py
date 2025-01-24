from __future__ import annotations

from ...base import VkObject


class DocTypes(VkObject):
    """VK Object DocsDocTypes

    count - Number of docs
    id - Doc type ID
    name - Doc type title
    """

    count: int
    id: int
    name: str
