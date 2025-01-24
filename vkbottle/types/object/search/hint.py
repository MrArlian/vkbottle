from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import SearchHintSection, SearchHintType

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_link import BaseLink
    from ..apps.app import App
    from ..groups.group import Group
    from ..users.user_min import UserMin


class Hint(VkObject):
    """VK Object SearchHint

    app -
    description - Object description
    _global - Information whether the object has been found globally
    group -
    link -
    profile -
    section -
    type -
    """

    app: Optional[App] = None
    description: str
    _global: Optional[bool] = None
    group: Optional[Group] = None
    link: Optional[BaseLink] = None
    profile: Optional[UserMin] = None
    section: Optional[SearchHintSection] = None
    type: SearchHintType
