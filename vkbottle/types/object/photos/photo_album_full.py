from __future__ import annotations

from typing import TYPE_CHECKING, Union, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .photo_sizes import PhotoSizes


class PhotoAlbumFull(VkObject):
    """VK Object PhotosPhotoAlbumFull

    can_delete - album can delete
    can_upload - Information whether current user can upload photo to the album
    comments_disabled - Information whether album comments are disabled
    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    sizes -
    thumb_id - Thumb photo ID
    thumb_is_last - Information whether the album thumb is last photo
    thumb_src - URL of the thumb image
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    upload_by_admins_only - Information whether only community administrators can upload photos
    """

    can_delete: Optional[bool] = None
    can_upload: Optional[bool] = None
    comments_disabled: Optional[bool] = None
    created: int
    description: Optional[str] = None
    id: int
    owner_id: int
    size: int
    sizes: Optional[List[PhotoSizes]] = None
    thumb_id: Optional[int] = None
    thumb_is_last: Optional[bool] = None
    thumb_src: Optional[str] = None
    title: str
    updated: int
    upload_by_admins_only: Optional[bool] = None


PhotosPhotoFalseable = Union[bool, str]
