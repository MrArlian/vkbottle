from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from .video import Video

if TYPE_CHECKING:
    from .video_files import VideoFiles
    from .live_settings import LiveSettings


class VideoFull(Video):
    """VK Object VideoVideoFull

    files -
    live_settings - Settings for live stream
    trailer -
    """

    files: Optional[VideoFiles] = None
    live_settings: Optional[LiveSettings] = None
    trailer: Optional[VideoFiles] = None
