from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import (
    PhotosTagsSuggestionItemButtonAction,
    PhotosTagsSuggestionItemButtonStyle
)

from ...base import VkObject


class TagsSuggestionItemButton(VkObject):
    """VK Object PhotosTagsSuggestionItemButton"""

    action: Optional[PhotosTagsSuggestionItemButtonAction] = None
    style: Optional[PhotosTagsSuggestionItemButtonStyle] = None
    title: Optional[str] = None
