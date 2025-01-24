from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AnimationScriptType

from ..base import VkObject


class BaseStickerAnimation(VkObject):
    """VK Object BaseStickerAnimation

    type - Type of animation script
    url - URL of animation script
    """

    type: Optional[AnimationScriptType] = None
    url: Optional[str] = None
