from __future__ import annotations

from typing import Optional

from ...base import VkObject


class UserConnections(VkObject):
    """VK Object UsersUserConnections

    facebook - User's Facebook account
    facebook_name - User's Facebook name
    instagram - User's Instagram account
    livejournal - User's Livejournal account
    skype - User's Skype nickname
    twitter - User's Twitter account
    """

    facebook: str
    facebook_name: Optional[str] = None
    instagram: str
    livejournal: Optional[str] = None
    skype: str
    twitter: str
