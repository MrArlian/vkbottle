from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .doc_preview_photo import DocPreviewPhoto
    from .doc_preview_audio_msg import DocPreviewAudioMsg
    from .doc_preview_graffiti import DocPreviewGraffiti
    from .doc_preview_video import DocPreviewVideo


class DocPreview(VkObject):
    """VK Object DocsDocPreview"""

    audio_msg: Optional[DocPreviewAudioMsg] = None
    graffiti: Optional[DocPreviewGraffiti] = None
    photo: Optional[DocPreviewPhoto] = None
    video: Optional[DocPreviewVideo] = None
