from __future__ import annotations

from vkbottle.enum.vk_object import NewsfeedNewsfeedItemType

from ...base import VkObject


class ItemBase(VkObject):
    """VK Object NewsfeedItemBase

    date - Date when item has been added in Unixtime
    source_id - Item source ID
    type -
    """

    date: int
    source_id: int
    type: NewsfeedNewsfeedItemType
