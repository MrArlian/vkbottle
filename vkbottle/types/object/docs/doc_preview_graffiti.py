from __future__ import annotations

from ...base import VkObject


class DocPreviewGraffiti(VkObject):
    """VK Object DocsDocPreviewGraffiti

    height - Graffiti height
    src - Graffiti file URL
    width - Graffiti width
    """

    height: int
    src: str
    width: int
