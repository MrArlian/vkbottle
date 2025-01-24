from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PhotoUpload(VkObject):
    """VK Object PhotosPhotoUpload

    album_id - Album ID
    fallback_upload_url - Fallback URL if upload_url returned error
    group_id - Group ID
    upload_url - URL to upload photo
    user_id - User ID
    """

    album_id: int
    fallback_upload_url: Optional[str] = None
    group_id: Optional[int] = None
    upload_url: str
    user_id: int
