from __future__ import annotations

from ..base import VkObject


class BaseUploadServer(VkObject):
    """VK Object BaseUploadServer

    upload_url - Upload URL
    """

    upload_url: str
