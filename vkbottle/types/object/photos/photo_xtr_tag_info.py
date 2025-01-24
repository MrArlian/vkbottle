from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .photo_sizes import PhotoSizes


class PhotoXtrTagInfo(VkObject):
    """VK Object PhotosPhotoXtrTagInfo

    access_key - Access key for the photo
    album_id - Album ID
    date - Date when uploaded
    height - Original photo height
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
    placer_id - ID of the tag creator
    post_id - Post ID
    sizes -
    tag_created - Date when tag has been added in Unixtime
    tag_id - Tag ID
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: int
    date: int
    height: Optional[int] = None
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
    placer_id: Optional[int] = None
    post_id: Optional[int] = None
    sizes: Optional[List[PhotoSizes]] = None
    tag_created: Optional[int] = None
    tag_id: Optional[int] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
