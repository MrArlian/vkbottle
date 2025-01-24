from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import WallPostSourceType

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_link import BaseLink


class PostSource(VkObject):
    """VK Object WallPostSource

    data - Additional data
    link -
    platform - Platform name
    type -
    url - URL to an external site used to publish the post
    """

    data: Optional[str] = None
    link: Optional[BaseLink] = None
    platform: Optional[str] = None
    type: Optional[WallPostSourceType] = None
    url: Optional[str] = None
