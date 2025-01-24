from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import NewsfeedItemDigestButtonStyle

from ...base import VkObject


class ItemDigestButton(VkObject):
    """VK Object NewsfeedItemDigestButton"""

    style: Optional[NewsfeedItemDigestButtonStyle] = None
    title: str
