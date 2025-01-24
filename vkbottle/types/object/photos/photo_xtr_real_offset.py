from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import BasePropertyExists

from ...base import VkObject

if TYPE_CHECKING:
    from .photo_sizes import PhotoSizes


class PhotoXtrRealOffset(VkObject):
    """VK Object PhotosPhotoXtrRealOffset

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
    hidden - Returns if the photo is hidden above the wall
    id - Photo ID
    lat - Latitude
    long - Longitude
    owner_id - Photo owner's ID
    photo_1280 - URL of image with 1280 px width
    photo_130 - URL of image with 130 px width
    photo_2560 - URL of image with 2560 px width
    photo_604 - URL of image with 604 px width
    photo_75 - URL of image with 75 px width
    photo_807 - URL of image with 807 px width
    post_id - Post ID
    real_offset - Real position of the photo
    sizes -
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: int
    date: int
    height: Optional[int] = None
    hidden: Optional[BasePropertyExists] = None
    id: int
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: int
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    sizes: Optional[List[PhotoSizes]] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
