from __future__ import annotations

from typing import Optional

from ...base import VkObject


class UserCounters(VkObject):
    """VK Object UsersUserCounters

    albums - Albums number
    articles -
    audios - Audios number
    badges - Badges number
    clips -
    clips_followers -
    followers - Followers number
    friends - Friends number
    gifts - Gifts number
    groups - Communities number
    mutual_friends -
    new_photo_tags -
    new_recognition_tags -
    notes - Notes number
    online_friends - Online friends number
    pages - Public pages number
    photos - Photos number
    podcasts -
    posts -
    subscriptions - Subscriptions number
    user_photos - Number of photos with user
    user_videos - Number of videos with user
    videos - Videos number
    wishes -
    """

    albums: Optional[int] = None
    articles: Optional[int] = None
    audios: Optional[int] = None
    badges: Optional[int] = None
    clips: Optional[int] = None
    clips_followers: Optional[int] = None
    followers: Optional[int] = None
    friends: Optional[int] = None
    gifts: Optional[int] = None
    groups: Optional[int] = None
    mutual_friends: Optional[int] = None
    new_photo_tags: Optional[int] = None
    new_recognition_tags: Optional[int] = None
    notes: Optional[int] = None
    online_friends: Optional[int] = None
    pages: Optional[int] = None
    photos: Optional[int] = None
    podcasts: Optional[int] = None
    posts: Optional[int] = None
    subscriptions: Optional[int] = None
    user_photos: Optional[int] = None
    user_videos: Optional[int] = None
    videos: Optional[int] = None
    wishes: Optional[int] = None
