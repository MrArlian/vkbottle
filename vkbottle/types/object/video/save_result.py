from __future__ import annotations

from typing import Optional

from ...base import VkObject


class SaveResult(VkObject):
    """VK Object VideoSaveResult

    access_key - Video access key
    description - Video description
    owner_id - Video owner ID
    title - Video title
    upload_url - URL for the video uploading
    video_id - Video ID
    """

    access_key: Optional[str] = None
    description: Optional[str] = None
    owner_id: Optional[int] = None
    title: Optional[str] = None
    upload_url: Optional[str] = None
    video_id: Optional[int] = None
