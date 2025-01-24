from __future__ import annotations

from typing import Optional

from ...base import VkObject


class VideoFiles(VkObject):
    """VK Object VideoVideoFiles

    external - URL of the external player
    flv_320 - URL of the flv file with 320p quality
    mp4_1080 - URL of the mpeg4 file with 1080p quality
    mp4_144 - URL of the mpeg4 file with 144p quality
    mp4_1440 - URL of the mpeg4 file with 2K quality
    mp4_2160 - URL of the mpeg4 file with 4K quality
    mp4_240 - URL of the mpeg4 file with 240p quality
    mp4_360 - URL of the mpeg4 file with 360p quality
    mp4_480 - URL of the mpeg4 file with 480p quality
    mp4_720 - URL of the mpeg4 file with 720p quality
    """

    external: Optional[str] = None
    flv_320: Optional[str] = None
    mp4_1080: Optional[str] = None
    mp4_144: Optional[str] = None
    mp4_1440: Optional[str] = None
    mp4_2160: Optional[str] = None
    mp4_240: Optional[str] = None
    mp4_360: Optional[str] = None
    mp4_480: Optional[str] = None
    mp4_720: Optional[str] = None
