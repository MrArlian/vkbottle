from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import BasePropertyExists

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_likes import BaseLikes
    from .photo_sizes import PhotoSizes
    from ..base_object_count import BaseObjectCount


class PhotoFullXtrRealOffset(VkObject):
    """VK Object PhotosPhotoFullXtrRealOffset

    access_key - Access key for the photo
    album_id - Album ID
    can_comment -
    comments -
    date - Date when uploaded
    height - Original photo height
    hidden - Returns if the photo is hidden above the wall
    id - Photo ID
    lat - Latitude
    likes -
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
    reposts -
    sizes -
    tags -
    text - Photo caption
    user_id - ID of the user who have uploaded the photo
    width - Original photo width
    """

    access_key: Optional[str] = None
    album_id: int
    can_comment: Optional[bool] = None
    comments: Optional[BaseObjectCount] = None
    date: int
    height: Optional[int] = None
    hidden: Optional[BasePropertyExists] = None
    id: int
    lat: Optional[float] = None
    likes: Optional[BaseLikes] = None
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
    reposts: Optional[BaseObjectCount] = None
    sizes: Optional[List[PhotoSizes]] = None
    tags: Optional[BaseObjectCount] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
