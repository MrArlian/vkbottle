from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .user_settings_interest import UserSettingsInterest


class UserSettingsInterests(VkObject):
    """VK Object AccountUserSettingsInterests"""

    about: Optional[UserSettingsInterest] = None
    activities: Optional[UserSettingsInterest] = None
    books: Optional[UserSettingsInterest] = None
    games: Optional[UserSettingsInterest] = None
    interests: Optional[UserSettingsInterest] = None
    movies: Optional[UserSettingsInterest] = None
    music: Optional[UserSettingsInterest] = None
    quotes: Optional[UserSettingsInterest] = None
    tv: Optional[UserSettingsInterest] = None
