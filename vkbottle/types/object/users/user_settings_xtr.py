from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from vkbottle.enum.vk_object import UsersUserRelation, BaseSex

from ...base import VkObject

if TYPE_CHECKING:
    from .personal import Personal
    from .user_connections import UserConnections
    from ..base_city import BaseCity
    from ..base_country import BaseCountry
    from .user_min import UserMin
    from ..account.name_request import NameRequest
    from ..audio_audio import AudioAudio
    from ..account.user_settings_interests import UserSettingsInterests


class UserSettingsXtr(VkObject):
    """VK Object UsersUserSettingsXtr

    bdate - User's date of birth
    bdate_visibility - Information whether user's birthdate are hidden
    city -
    connections -
    country -
    first_name - User first name
    home_town - User's hometown
    interests -
    languages -
    last_name - User last name
    maiden_name - User maiden name
    name_request -
    personal -
    phone - User phone number with some hidden digits
    relation - User relationship status
    relation_partner -
    relation_pending - Information whether relation status is pending
    relation_requests -
    screen_name - Domain name of the user's page
    sex - User sex
    status - User status
    status_audio -
    """

    bdate: Optional[str] = None
    bdate_visibility: Optional[int] = None
    city: Optional[BaseCity] = None
    connections: Optional[UserConnections] = None
    country: Optional[BaseCountry] = None
    first_name: Optional[str] = None
    home_town: str
    interests: Optional[UserSettingsInterests] = None
    languages: Optional[List[str]] = None
    last_name: Optional[str] = None
    maiden_name: Optional[str] = None
    name_request: Optional[NameRequest] = None
    personal: Optional[Personal] = None
    phone: Optional[str] = None
    relation: Optional[UsersUserRelation] = None
    relation_partner: Optional[UserMin] = None
    relation_pending: Optional[bool] = None
    relation_requests: Optional[List[UserMin]] = None
    screen_name: Optional[str] = None
    sex: Optional[BaseSex] = None
    status: str
    status_audio: Optional[AudioAudio] = None
