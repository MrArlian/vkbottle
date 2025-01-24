from __future__ import annotations

from typing import Optional

from ...base import VkObject


class AccountCounters(VkObject):
    """VK Object AccountAccountCounters

    app_requests - New app requests number
    events - New events number
    faves - New faves number
    friends - New friends requests number
    friends_recommendations - New friends recommendations number
    friends_suggestions - New friends suggestions number
    gifts - New gifts number
    groups - New groups number
    memories - New memories number
    menu_clips_badge -
    menu_discover_badge -
    messages - New messages number
    notes - New notes number
    notifications - New notifications number
    photos - New photo tags number
    sdk - New sdk number
    """

    app_requests: Optional[int] = None
    events: Optional[int] = None
    faves: Optional[int] = None
    friends: Optional[int] = None
    friends_recommendations: Optional[int] = None
    friends_suggestions: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    memories: Optional[int] = None
    menu_clips_badge: Optional[int] = None
    menu_discover_badge: Optional[int] = None
    messages: Optional[int] = None
    notes: Optional[int] = None
    notifications: Optional[int] = None
    photos: Optional[int] = None
    sdk: Optional[int] = None
