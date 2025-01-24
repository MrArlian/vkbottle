from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import PhotosPhotoSizesType

from ...base import VkObject


class PhotoSizes(VkObject):
    """VK Object PhotosPhotoSizes

    height - Height in px
    src - URL of the image
    type -
    url - URL of the image
    width - Width in px
    """

    height: int
    src: Optional[str] = None
    type: PhotosPhotoSizesType
    url: str
    width: int
