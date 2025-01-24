from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .doc_preview_photo_sizes import DocPreviewPhotoSizes


class DocPreviewPhoto(VkObject):
    """VK Object DocsDocPreviewPhoto"""

    sizes: Optional[List[DocPreviewPhotoSizes]] = None
