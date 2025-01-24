from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .photo import Photo


class PhotoAlbum(VkObject):
    """VK Object PhotosPhotoAlbum

    created - Date when the album has been created in Unixtime
    description - Photo album description
    id - Photo album ID
    owner_id - Album owner's ID
    size - Photos number
    thumb -
    title - Photo album title
    updated - Date when the album has been updated last time in Unixtime
    """

    created: int
    description: Optional[str] = None
    id: int
    owner_id: int
    size: int
    thumb: Optional[Photo] = None
    title: str
    updated: int
