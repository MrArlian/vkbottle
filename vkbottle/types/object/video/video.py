from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import VideoVideoType, LiveStreamStatus, BasePropertyExists

from ...base import VkObject

if TYPE_CHECKING:
    from ..base_likes import BaseLikes
    from ..base_reposts_info import BaseRepostsInfo
    from .video_image import VideoImage


class Video(VkObject):
    """VK Object VideoVideo

    access_key - Video access key
    added - 1 if video is added to user's albums
    adding_date - Date when the video has been added in Unixtime
    balance - Live donations balance
    can_add - Information whether current user can add the video
    can_add_to_faves - Information whether current user can add the video to favourites
    can_attach_link - Information whether current user can attach action button to the video
    can_comment - Information whether current user can comment the video
    can_edit - Information whether current user can edit the video
    can_like - Information whether current user can like the video
    can_repost - Information whether current user can repost the video
    can_subscribe - Information whether current user can subscribe to author of the video
    comments - Number of comments
    content_restricted - Restriction code
    content_restricted_message - Restriction text
    converting - 1 if  video is being converted
    date - Date when video has been uploaded in Unixtime
    description - Video description
    duration - Video duration in seconds
    first_frame -
    height - Video height
    id - Video ID
    image -
    is_favorite - Whether video is added to bookmarks
    is_private - 1 if video is private
    is_subscribed - 1 if user is subscribed to author of the video
    likes -
    live - 1 if the video is a live stream
    live_notify - Whether current user is subscribed to the upcoming live stream notification (if not subscribed to the author)
    live_start_time - Date in Unixtime when the live stream is scheduled to start by the author
    live_status - Live stream status
    local_views - If video is external, number of views on vk
    owner_id - Video owner ID
    platform - External platform
    player - Video embed URL
    processing - Returns if the video is processing
    repeat - Information whether the video is repeated
    reposts -
    spectators - Number of spectators of the stream
    title - Video title
    track_code -
    type -
    upcoming - 1 if the video is an upcoming stream
    user_id - Id of the user who uploaded the video if it was uploaded to a group by member
    views - Number of views
    width - Video width
    """

    access_key: Optional[str] = None
    added: Optional[bool] = None
    adding_date: Optional[int] = None
    balance: Optional[int] = None
    can_add: Optional[bool] = None
    can_add_to_faves: Optional[bool] = None
    can_attach_link: Optional[bool] = None
    can_comment: Optional[bool] = None
    can_edit: Optional[bool] = None
    can_like: Optional[bool] = None
    can_repost: Optional[bool] = None
    can_subscribe: Optional[bool] = None
    comments: Optional[int] = None
    content_restricted: Optional[int] = None
    content_restricted_message: Optional[str] = None
    converting: Optional[bool] = None
    date: Optional[int] = None
    description: Optional[str] = None
    duration: Optional[int] = None
    first_frame: Optional[List[VideoImage]] = None
    height: Optional[int] = None
    id: Optional[int] = None
    image: Optional[List[VideoImage]] = None
    is_favorite: Optional[bool] = None
    is_private: Optional[bool] = None
    is_subscribed: Optional[bool] = None
    likes: Optional[BaseLikes] = None
    live: Optional[BasePropertyExists] = None
    live_notify: Optional[bool] = None
    live_start_time: Optional[int] = None
    live_status: Optional[LiveStreamStatus] = None
    local_views: Optional[int] = None
    owner_id: Optional[int] = None
    platform: Optional[str] = None
    player: Optional[str] = None
    processing: Optional[BasePropertyExists] = None
    repeat: Optional[BasePropertyExists] = None
    reposts: Optional[BaseRepostsInfo] = None
    spectators: Optional[int] = None
    title: Optional[str] = None
    track_code: Optional[str] = None
    type: Optional[VideoVideoType] = None
    upcoming: Optional[BasePropertyExists] = None
    user_id: Optional[int] = None
    views: Optional[int] = None
    width: Optional[int] = None
