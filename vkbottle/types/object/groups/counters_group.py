from __future__ import annotations

from typing import Optional

from ...base import VkObject


class CountersGroup(VkObject):
    """VK Object GroupsCountersGroup

    addresses - Addresses number
    albums - Photo albums number
    articles - Articles number
    audio_playlists - Audio playlists number
    audios - Audios number
    clips - Clips number
    clips_followers - Clips followers number
    docs - Docs number
    market - Market items number
    market_services - Market services number
    narratives - Narratives number
    photos - Photos number
    podcasts - Podcasts number
    topics - Topics number
    videos - Videos number
    """

    addresses: Optional[int] = None
    albums: Optional[int] = None
    articles: Optional[int] = None
    audio_playlists: Optional[int] = None
    audios: Optional[int] = None
    clips: Optional[int] = None
    clips_followers: Optional[int] = None
    docs: Optional[int] = None
    market: Optional[int] = None
    market_services: Optional[int] = None
    narratives: Optional[int] = None
    photos: Optional[int] = None
    podcasts: Optional[int] = None
    topics: Optional[int] = None
    videos: Optional[int] = None
