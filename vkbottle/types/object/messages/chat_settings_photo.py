from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ChatSettingsPhoto(VkObject):
    """VK Object MessagesChatSettingsPhoto

    is_default_call_photo - If provided photo is default call photo
    is_default_photo - If provided photo is default
    photo_100 - URL of the preview image with 100px in width
    photo_200 - URL of the preview image with 200px in width
    photo_50 - URL of the preview image with 50px in width
    """

    is_default_call_photo: Optional[bool] = None
    is_default_photo: Optional[bool] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
