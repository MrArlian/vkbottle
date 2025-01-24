from __future__ import annotations

from typing import TYPE_CHECKING, Optional, List, Union

from vkbottle.enum.vk_object import UsersUserRelation, UsersUserType, UsersUserFullWallDefault

from .user import User

if TYPE_CHECKING:
    from ..base_city import BaseCity
    from ..base_country import BaseCountry
    from ..base_crop_photo import BaseCropPhoto
    from .career import Career
    from .user_counters import UserCounters
    from .exports import Exports
    from .last_seen import LastSeen
    from .military import Military
    from .occupation import Occupation
    from ..owner_state import OwnerState
    from .personal import Personal
    from ..photos.photo import Photo
    from .user_min import UserMin
    from .relative import Relative
    from .school import School
    from .university import University
    from ..audio_audio import AudioAudio
    from ..video.live_info import LiveInfo


PhotosPhotoFalseable = Union[bool, str]


class UserFull(User):
    """VK Object UsersUserFull

    about -
    access_key -
    activities -
    activity - User's status
    bdate - User's date of birth
    blacklisted - Information whether current user is in the requested user's blacklist.
    blacklisted_by_me - Information whether the requested user is in current user's blacklist
    books -
    can_be_invited_group - Information whether current user can be invited to the community
    can_call - Information whether current user can call
    can_call_from_group - Information whether group can call user
    can_post - Information whether current user can post on the user's wall
    can_see_all_posts - Information whether current user can see other users' audio on the wall
    can_see_audio - Information whether current user can see the user's audio
    can_see_gifts - Information whether current user can see the user's gifts
    can_see_wishes - Information whether current user can see the user's wishes
    can_send_friend_request - Information whether current user can send a friend request
    can_subscribe_podcasts - Owner in whitelist or not
    can_subscribe_posts - Can subscribe to wall
    can_upload_doc -
    can_write_private_message - Information whether current user can write private message
    career -
    city -
    clips_count - Number of user's clips
    common_count - Number of common friends with current user
    contact_id - Contact person ID
    contact_name - User contact name
    counters -
    country -
    crop_photo -
    descriptions -
    domain - Domain name of the user's page
    education_form - Education form
    education_status - User's education status
    email -
    exports -
    facebook -
    facebook_name -
    faculty - Faculty ID
    faculty_name - Faculty name
    first_name_abl - User's first name in prepositional case
    first_name_acc - User's first name in accusative case
    first_name_dat - User's first name in dative case
    first_name_gen - User's first name in genitive case
    first_name_ins - User's first name in instrumental case
    first_name_nom - User's first name in nominative case
    followers_count - Number of user's followers
    games -
    graduation - Graduation year
    has_mobile - Information whether the user specified his phone number
    has_photo - Information whether the user has main photo
    has_unseen_stories -
    hash -
    home_phone - User's additional phone number
    home_town - User hometown
    instagram -
    interests -
    is_favorite - Information whether the requested user is in faves of current user
    is_friend - Information whether the user is a friend of current user
    is_hidden_from_feed - Information whether the requested user is hidden from current user's newsfeed
    is_message_request -
    is_no_index - Access to user profile is restricted for search engines
    is_service -
    is_subscribed_podcasts - Information whether current user is subscribed to podcasts
    is_video_live_notifications_blocked -
    language -
    last_name_abl - User's last name in prepositional case
    last_name_acc - User's last name in accusative case
    last_name_dat - User's last name in dative case
    last_name_gen - User's last name in genitive case
    last_name_ins - User's last name in instrumental case
    last_name_nom - User's last name in nominative case
    last_seen -
    lists -
    livejournal -
    maiden_name - User maiden name
    military -
    mobile_phone - User's mobile phone number
    movies -
    music -
    nickname - User nickname
    occupation -
    owner_state -
    personal -
    photo -
    photo_200 - URL of square photo of the user with 200 pixels in width
    photo_200_orig - URL of user's photo with 200 pixels in width
    photo_400 -
    photo_400_orig - URL of user's photo with 400 pixels in width
    photo_big -
    photo_id - ID of the user's main photo
    photo_max - URL of square photo of the user with maximum width
    photo_max_orig - URL of user's photo of maximum size
    photo_max_size -
    photo_medium -
    photo_medium_rec -
    photo_rec -
    quotes -
    relation - User relationship status
    relation_partner -
    relatives -
    schools -
    service_description -
    site - User's website
    skype -
    status - User's status
    status_audio -
    stories_archive_count -
    test -
    timezone - User's timezone
    tv -
    twitter -
    type -
    universities -
    university - University ID
    university_group_id -
    university_name - University name
    video_live -
    video_live_count - Number of user's live streams
    video_live_level - User level in live streams achievements
    wall_comments - Information whether current user can comment wall posts
    wall_default -
    """

    about: Optional[str] = None
    access_key: Optional[str] = None
    activities: Optional[str] = None
    activity: Optional[str] = None
    bdate: Optional[str] = None
    blacklisted: Optional[bool] = None
    blacklisted_by_me: Optional[bool] = None
    books: Optional[str] = None
    can_be_invited_group: Optional[bool] = None
    can_call: Optional[bool] = None
    can_call_from_group: Optional[bool] = None
    can_post: Optional[bool] = None
    can_see_all_posts: Optional[bool] = None
    can_see_audio: Optional[bool] = None
    can_see_gifts: Optional[bool] = None
    can_see_wishes: Optional[bool] = None
    can_send_friend_request: Optional[bool] = None
    can_subscribe_podcasts: Optional[bool] = None
    can_subscribe_posts: Optional[bool] = None
    can_upload_doc: Optional[bool] = None
    can_write_private_message: Optional[bool] = None
    career: Optional[List[Career]] = None
    city: Optional[BaseCity] = None
    clips_count: Optional[int] = None
    common_count: Optional[int] = None
    contact_id: Optional[int] = None
    contact_name: Optional[str] = None
    counters: Optional[UserCounters] = None
    country: Optional[BaseCountry] = None
    crop_photo: Optional[BaseCropPhoto] = None
    descriptions: Optional[List[str]] = None
    domain: Optional[str] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    email: Optional[str] = None
    exports: Optional[Exports] = None
    facebook: Optional[str] = None
    facebook_name: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    first_name_abl: Optional[str] = None
    first_name_acc: Optional[str] = None
    first_name_dat: Optional[str] = None
    first_name_gen: Optional[str] = None
    first_name_ins: Optional[str] = None
    first_name_nom: Optional[str] = None
    followers_count: Optional[int] = None
    games: Optional[str] = None
    graduation: Optional[int] = None
    has_mobile: Optional[bool] = None
    has_photo: Optional[bool] = None
    has_unseen_stories: Optional[bool] = None
    hash: Optional[str] = None
    home_phone: Optional[str] = None
    home_town: Optional[str] = None
    instagram: Optional[str] = None
    interests: Optional[str] = None
    is_favorite: Optional[bool] = None
    is_friend: Optional[bool] = None
    is_hidden_from_feed: Optional[bool] = None
    is_message_request: Optional[bool] = None
    is_no_index: Optional[bool] = None
    is_service: Optional[bool] = None
    is_subscribed_podcasts: Optional[bool] = None
    is_video_live_notifications_blocked: Optional[bool] = None
    language: Optional[str] = None
    last_name_abl: Optional[str] = None
    last_name_acc: Optional[str] = None
    last_name_dat: Optional[str] = None
    last_name_gen: Optional[str] = None
    last_name_ins: Optional[str] = None
    last_name_nom: Optional[str] = None
    last_seen: Optional[LastSeen] = None
    lists: Optional[List[int]] = None
    livejournal: Optional[str] = None
    maiden_name: Optional[str] = None
    military: Optional[List[Military]] = None
    mobile_phone: Optional[str] = None
    movies: Optional[str] = None
    music: Optional[str] = None
    nickname: Optional[str] = None
    occupation: Optional[Occupation] = None
    owner_state: Optional[OwnerState] = None
    personal: Optional[Personal] = None
    photo: Optional[str] = None
    photo_200: Optional[str] = None
    photo_200_orig: Optional[str] = None
    photo_400: Optional[str] = None
    photo_400_orig: Optional[str] = None
    photo_big: Optional[str] = None
    photo_id: Optional[str] = None
    photo_max: Optional[str] = None
    photo_max_orig: Optional[str] = None
    photo_max_size: Optional[Photo] = None
    photo_medium: Optional[PhotosPhotoFalseable] = None
    photo_medium_rec: Optional[PhotosPhotoFalseable] = None
    photo_rec: Optional[PhotosPhotoFalseable] = None
    quotes: Optional[str] = None
    relation: Optional[UsersUserRelation] = None
    relation_partner: Optional[UserMin] = None
    relatives: Optional[List[Relative]] = None
    schools: Optional[List[School]] = None
    service_description: Optional[str] = None
    site: Optional[str] = None
    skype: Optional[str] = None
    status: Optional[str] = None
    status_audio: Optional[AudioAudio] = None
    stories_archive_count: Optional[int] = None
    test: Optional[bool] = None
    timezone: Optional[float] = None
    tv: Optional[str] = None
    twitter: Optional[str] = None
    type: Optional[UsersUserType] = None
    universities: Optional[List[University]] = None
    university: Optional[int] = None
    university_group_id: Optional[int] = None
    university_name: Optional[str] = None
    video_live: Optional[LiveInfo] = None
    video_live_count: Optional[int] = None
    video_live_level: Optional[int] = None
    wall_comments: Optional[bool] = None
    wall_default: Optional[UsersUserFullWallDefault] = None
