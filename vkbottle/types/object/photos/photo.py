from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_reposts_info import BaseRepostsInfo
    from .photo_sizes import PhotoSizes
    from ..base_object_count import BaseObjectCount
    from ..base_likes import BaseLikes
    from .image import Image


class Photo(VkObject):
    """VK Object PhotosPhoto

    access_key - Access key for the photo
    album_id - Album ID
    can_comment - Information whether current user can comment the photo
    comments -
    date - Date when uploaded
    has_tags - Whether photo has attached tag links
    height - Original photo height
    id - Photo ID
    images -
    lat - Latitude
    likes -
    long - Longitude
    owner_id - Photo owner's ID
    photo_256 - URL of image with 2560 px width
    place -
    post_id - Post ID
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
    has_tags: bool
    height: Optional[int] = None
    id: int
    images: Optional[List[Image]] = None
    lat: Optional[float] = None
    likes: Optional[BaseLikes] = None
    long: Optional[float] = None
    owner_id: int
    photo_256: Optional[str] = None
    place: Optional[str] = None
    post_id: Optional[int] = None
    reposts: Optional[BaseRepostsInfo] = None
    sizes: Optional[List[PhotoSizes]] = None
    tags: Optional[BaseObjectCount] = None
    text: Optional[str] = None
    user_id: int = None
    width: Optional[int] = None
