from __future__ import annotations

from ...base import VkObject


class DocPreviewVideo(VkObject):
    """VK Object DocsDocPreviewVideo

    file_size - Video file size in bites
    height - Video's height in pixels
    src - Video URL
    width - Video's width in pixels
    """

    file_size: int
    height: int
    src: str
    width: int
