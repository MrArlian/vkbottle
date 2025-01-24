from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import BasePropertyExists

from ..base_image import BaseImage


class VideoImage(BaseImage):
    """VK Object VideoVideoImage"""

    with_padding: Optional[BasePropertyExists] = None
