from __future__ import annotations

from vkbottle.enum.vk_object import PhotosPhotoSizesType

from ...base import VkObject


class DocPreviewPhotoSizes(VkObject):
    """VK Object DocsDocPreviewPhotoSizes

    height - Height in px
    src - URL of the image
    type -
    width - Width in px
    """

    height: int
    src: str
    type: PhotosPhotoSizesType
    width: int
