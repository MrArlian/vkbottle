from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import BaseLinkButtonStyle

from ..base import VkObject

if TYPE_CHECKING:
    from .base_link_button_action import BaseLinkButtonAction


class BaseLinkButton(VkObject):
    """VK Object BaseLinkButton

    action - Button action
    album_id - Video album id
    block_id - Target block id
    curator_id - curator id
    icon - Button icon name, e.g. 'phone' or 'gift'
    owner_id - Owner id
    section_id - Target section id
    style -
    title - Button title
    """

    action: Optional[BaseLinkButtonAction] = None
    album_id: Optional[int] = None
    block_id: Optional[str] = None
    curator_id: Optional[int] = None
    icon: Optional[str] = None
    owner_id: Optional[int] = None
    section_id: Optional[str] = None
    style: Optional[BaseLinkButtonStyle] = None
    title: Optional[str] = None
