from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import NewsfeedItemDigestHeaderStyle

from ...base import VkObject

if TYPE_CHECKING:
    from .item_digest_button import ItemDigestButton


class ItemDigestHeader(VkObject):
    """VK Object NewsfeedItemDigestHeader

    button -
    style -
    subtitle - Subtitle of the header, when title have two strings
    title - Title of the header
    """

    button: Optional[ItemDigestButton] = None
    style: NewsfeedItemDigestHeaderStyle
    subtitle: Optional[str] = None
    title: str
