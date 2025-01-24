from __future__ import annotations

from typing import Optional, List

from vkbottle.enum.vk_object import AppsAppLeaderboardType

from .app_min import AppMin


class App(AppMin):
    """VK Object AppsApp

    author_url - Application author's URL
    banner_1120 - URL of the app banner with 1120 px in width
    banner_560 - URL of the app banner with 560 px in width
    catalog_position - Catalog position
    description - Application description
    friends -
    genre - Genre name
    genre_id - Genre ID
    icon_16 - URL of the app icon with 16 px in width
    international - Information whether the application is multilanguage
    is_in_catalog - Information whether application is in mobile catalog
    is_new - Is new flag
    leaderboard_type -
    members_count - Members number
    platform_id - Application ID in store
    published_date - Date when the application has been published in Unixtime
    push_enabled - Is push enabled
    screen_name - Screen name
    screen_orientation - Screen orientation
    section - Application section name
    """

    author_url: Optional[str] = None
    banner_1120: Optional[str] = None
    banner_560: Optional[str] = None
    catalog_position: Optional[int] = None
    description: Optional[str] = None
    friends: Optional[List[int]] = None
    genre: Optional[str] = None
    genre_id: Optional[int] = None
    icon_16: Optional[str] = None
    international: Optional[bool] = None
    is_in_catalog: Optional[int] = None
    is_new: Optional[bool] = None
    leaderboard_type: Optional[AppsAppLeaderboardType] = None
    members_count: Optional[int] = None
    platform_id: Optional[str] = None
    published_date: Optional[int] = None
    push_enabled: Optional[bool] = None
    screen_name: Optional[str] = None
    screen_orientation: Optional[int] = None
    section: Optional[str] = None
