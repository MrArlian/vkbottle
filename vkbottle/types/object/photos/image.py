from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import PhotosImageType

from ...base import VkObject


class Image(VkObject):
    """VK Object PhotosImage

    height - Height of the photo in px.
    type -
    url - Photo URL.
    width - Width of the photo in px.
    """

    height: Optional[int] = None
    type: Optional[PhotosImageType] = None
    url: Optional[str] = None
    width: Optional[int] = None
