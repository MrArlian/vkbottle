from __future__ import annotations

from ...base import VkObject


class VideoAlbum(VkObject):
    """VK Object VideoVideoAlbum

    id - Album ID
    owner_id - Album owner's ID
    title - Album title
    """

    id: int
    owner_id: int
    title: str
