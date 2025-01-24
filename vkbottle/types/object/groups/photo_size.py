from __future__ import annotations

from ...base import VkObject


class PhotoSize(VkObject):
    """VK Object GroupsPhotoSize

    height - Image height
    width - Image width
    """

    height: int
    width: int
