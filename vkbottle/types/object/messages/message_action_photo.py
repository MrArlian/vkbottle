from __future__ import annotations

from ...base import VkObject


class MessageActionPhoto(VkObject):
    """VK Object MessagesMessageActionPhoto

    photo_100 - URL of the preview image with 100px in width
    photo_200 - URL of the preview image with 200px in width
    photo_50 - URL of the preview image with 50px in width
    """

    photo_100: str
    photo_200: str
    photo_50: str
