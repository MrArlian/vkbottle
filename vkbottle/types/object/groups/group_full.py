from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List

from vkbottle.enum.vk_object import (
    GroupsGroupFullAgeLimits,
    GroupsGroupFullSection,
    GroupsGroupFullMemberStatus,
    GroupsGroupFullWall
)

from .group import Group

if TYPE_CHECKING:
    from ..base_object import BaseObject
    from .addresses_info import AddressesInfo
    from .group_ban_info import GroupBanInfo
    from .contacts_item import ContactsItem
    from .counters_group import CountersGroup
    from .cover import Cover
    from .links_item import LinksItem
    from .live_covers import LiveCovers
    from .market_info import MarketInfo
    from .online_status import OnlineStatus
    from ..audio_audio import AudioAudio
    from ..base_country import BaseCountry
    from ..base_crop_photo import BaseCropPhoto


class GroupFull(Group):
    """VK Object GroupsGroupFull

    activity - Type of group, start date of event or category of public page
    addresses - Info about addresses in groups
    age_limits - Information whether age limit
    ban_info - User ban info
    can_create_topic - Information whether current user can create topic
    can_message - Information whether current user can send a message to community
    can_post - Information whether current user can post on community's wall
    can_see_all_posts - Information whether current user can see all posts on community's wall
    can_send_notify - Information whether community can send notifications by phone number to current user
    can_subscribe_podcasts - Owner in whitelist or not
    can_subscribe_posts - Can subscribe to wall
    can_suggest -
    can_upload_doc - Information whether current user can upload doc
    can_upload_story - Information whether current user can upload story
    can_upload_video - Information whether current user can upload video
    city -
    clips_count - Number of community's clips
    contacts -
    counters -
    country -
    cover -
    crop_photo - Данные о точках, по которым вырезаны профильная и миниатюрная фотографии сообщества
    description - Community description
    fixed_post - Fixed post ID
    has_group_channel -
    has_market_app - Information whether community has installed market app
    has_photo - Information whether community has photo
    has_unseen_stories -
    invited_by - Inviter ID
    is_adult - Information whether community is adult
    is_favorite - Information whether community is in faves
    is_hidden_from_feed - Information whether community is hidden from current user's newsfeed
    is_messages_blocked - Information whether community can send a message to current user
    is_subscribed - Information whether current user is subscribed
    is_subscribed_podcasts - Information whether current user is subscribed to podcasts
    links -
    live_covers - Live covers state
    main_album_id - Community's main photo album ID
    main_section -
    market -
    member_status - Current user's member status
    members_count - Community members number
    members_count_text - Info about number of users in group
    online_status - Status of replies in community messages
    requests_count - The number of incoming requests to the community
    secondary_section -
    site - Community's website
    status - Community status
    status_audio -
    stories_archive_count -
    trending - Information whether the community has a "fire" pictogram.
    using_vkpay_market_app -
    verified - Information whether community is verified
    video_live_count - Number of community's live streams
    video_live_level - Community level live streams achievements
    wall - Information about wall status in community
    wiki_page - Community's main wiki page title
    """

    activity: Optional[str] = None
    addresses: Optional[AddressesInfo] = None
    age_limits: Optional[GroupsGroupFullAgeLimits] = None
    ban_info: Optional[GroupBanInfo] = None
    can_create_topic: Optional[bool] = None
    can_message: Optional[bool] = None
    can_post: Optional[bool] = None
    can_see_all_posts: Optional[bool] = None
    can_send_notify: Optional[bool] = None
    can_subscribe_podcasts: Optional[bool] = None
    can_subscribe_posts: Optional[bool] = None
    can_suggest: Optional[bool] = None
    can_upload_doc: Optional[bool] = None
    can_upload_story: Optional[bool] = None
    can_upload_video: Optional[bool] = None
    city: Optional[BaseObject] = None
    clips_count: Optional[int] = None
    contacts: Optional[List[ContactsItem]] = None
    counters: Optional[CountersGroup] = None
    country: Optional[BaseCountry] = None
    cover: Optional[Cover] = None
    crop_photo: Optional[BaseCropPhoto] = None
    description: Optional[str] = None
    fixed_post: Optional[int] = None
    has_group_channel: Optional[bool] = None
    has_market_app: Optional[bool] = None
    has_photo: Optional[bool] = None
    has_unseen_stories: Optional[bool] = None
    invited_by: Optional[int] = None
    is_adult: Optional[bool] = None
    is_favorite: Optional[bool] = None
    is_hidden_from_feed: Optional[bool] = None
    is_messages_blocked: Optional[bool] = None
    is_subscribed: Optional[bool] = None
    is_subscribed_podcasts: Optional[bool] = None
    links: Optional[List[LinksItem]] = None
    live_covers: Optional[LiveCovers] = None
    main_album_id: Optional[int] = None
    main_section: Optional[GroupsGroupFullSection] = None
    market: Optional[MarketInfo] = None
    member_status: Optional[GroupsGroupFullMemberStatus] = None
    members_count: Optional[int] = None
    members_count_text: Optional[str] = None
    online_status: Optional[OnlineStatus] = None
    requests_count: Optional[int] = None
    secondary_section: Optional[GroupsGroupFullSection] = None
    site: Optional[str] = None
    status: Optional[str] = None
    status_audio: Optional[AudioAudio] = None
    stories_archive_count: Optional[int] = None
    trending: Optional[bool] = None
    using_vkpay_market_app: Optional[bool] = None
    verified: Optional[bool] = None
    video_live_count: Optional[int] = None
    video_live_level: Optional[int] = None
    wall: Optional[GroupsGroupFullWall] = None
    wiki_page: Optional[str] = None


