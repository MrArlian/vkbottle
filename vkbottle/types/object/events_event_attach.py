from __future__ import annotations

from typing import List, Optional

from vkbottle.enum.vk_object import GroupsGroupFullMemberStatus

from ..base import VkObject


class EventsEventAttach(VkObject):
    """VK Object EventsEventAttach

    address - address of event
    button_text - text of attach
    friends - array of friends ids
    id - event ID
    is_favorite - is favorite
    member_status - Current user's member status
    text - text of attach
    time - event start time
    """

    address: Optional[str] = None
    button_text: str
    friends: List[int]
    id: int
    is_favorite: bool
    member_status: Optional[GroupsGroupFullMemberStatus] = None
    text: str
    time: Optional[int] = None
