from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import StoriesStoryType

from ...base import VkObject

if TYPE_CHECKING:
    from .story import Story
    from ..video.video_full import VideoFull
    from .replies import Replies
    from .story_link import StoryLink
    from ..photos.photo import Photo
    from .clickable_stickers import ClickableStickers


class Story(VkObject):
    """VK Object StoriesStory

    access_key - Access key for private object.
    birthday_wish_user_id -
    can_ask - Information whether story has question sticker and current user can send question to the author
    can_ask_anonymous - Information whether story has question sticker and current user can send anonymous question to the author
    can_comment - Information whether current user can comment the story (0 - no, 1 - yes).
    can_hide - Information whether current user can hide the story (0 - no, 1 - yes).
    can_like - Information whether current user can like the story.
    can_reply - Information whether current user can reply to the story (0 - no, 1 - yes).
    can_see - Information whether current user can see the story (0 - no, 1 - yes).
    can_share - Information whether current user can share the story (0 - no, 1 - yes).
    can_use_in_narrative -
    clickable_stickers -
    date - Date when story has been added in Unixtime.
    expires_at - Story expiration time. Unixtime.
    first_narrative_title -
    id - Story ID.
    is_deleted - Information whether the story is deleted (false - no, true - yes).
    is_expired - Information whether the story is expired (false - no, true - yes).
    link -
    narratives_count -
    owner_id - Story owner's ID.
    parent_story -
    parent_story_access_key - Access key for private object.
    parent_story_id - Parent story ID.
    parent_story_owner_id - Parent story owner's ID.
    photo -
    replies - Replies counters to current story.
    seen - Information whether current user has seen the story or not (0 - no, 1 - yes).
    type -
    video -
    views - Views number.
    """

    access_key: Optional[str] = None
    birthday_wish_user_id: Optional[int] = None
    can_ask: Optional[bool] = None
    can_ask_anonymous: Optional[bool] = None
    can_comment: Optional[bool] = None
    can_hide: Optional[bool] = None
    can_like: Optional[bool] = None
    can_reply: Optional[bool] = None
    can_see: Optional[bool] = None
    can_share: Optional[bool] = None
    can_use_in_narrative: Optional[bool] = None
    clickable_stickers: Optional[ClickableStickers] = None
    date: Optional[int] = None
    expires_at: Optional[int] = None
    first_narrative_title: Optional[str] = None
    id: int
    is_deleted: Optional[bool] = None
    is_expired: Optional[bool] = None
    link: Optional[StoryLink] = None
    narratives_count: Optional[int] = None
    owner_id: int
    parent_story: Optional[Story] = None
    parent_story_access_key: Optional[str] = None
    parent_story_id: Optional[int] = None
    parent_story_owner_id: Optional[int] = None
    photo: Optional[Photo] = None
    replies: Optional[Replies] = None
    seen: Optional[bool] = None
    type: Optional[StoriesStoryType] = None
    video: Optional[VideoFull] = None
    views: Optional[int] = None
