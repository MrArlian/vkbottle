from __future__ import annotations

from typing import TYPE_CHECKING

from ..base import VkObject

if TYPE_CHECKING:
    from .base_crop_photo_rect import BaseCropPhotoRect
    from .photos.photo import Photo
    from .base_crop_photo_crop import BaseCropPhotoCrop


class BaseCropPhoto(VkObject):
    """VK Object BaseCropPhoto"""

    crop: BaseCropPhotoCrop
    photo: Photo
    rect: BaseCropPhotoRect
