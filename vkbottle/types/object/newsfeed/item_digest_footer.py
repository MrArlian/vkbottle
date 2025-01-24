from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import NewsfeedItemDigestFooterStyle

from ...base import VkObject

if TYPE_CHECKING:
    from .item_digest_button import ItemDigestButton


class ItemDigestFooter(VkObject):
    """VK Object NewsfeedItemDigestFooter

    button -
    style -
    text - text for invite to enable smart feed
    """

    button: Optional[ItemDigestButton] = None
    style: NewsfeedItemDigestFooterStyle
    text: str
