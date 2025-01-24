from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import BasePropertyExists, AdsCriteriaSex

from ...base import VkObject


class Criteria(VkObject):
    """VK Object AdsCriteria

    age_from - Age from
    age_to - Age to
    apps - Apps IDs
    apps_not - Apps IDs to except
    birthday - Days to birthday
    cities - Cities IDs
    cities_not - Cities IDs to except
    country - Country ID
    districts - Districts IDs
    groups - Communities IDs
    interest_categories - Interests categories IDs
    interests - Interests
    paying - Information whether the user has proceeded VK payments before
    positions - Positions IDs
    religions - Religions IDs
    retargeting_groups - Retargeting groups IDs
    retargeting_groups_not - Retargeting groups IDs to except
    school_from - School graduation year from
    school_to - School graduation year to
    schools - Schools IDs
    sex -
    stations - Stations IDs
    statuses - Relationship statuses
    streets - Streets IDs
    travellers - Travellers only
    uni_from - University graduation year from
    uni_to - University graduation year to
    user_browsers - Browsers
    user_devices - Devices
    user_os - Operating systems
    """

    age_from: Optional[int] = None
    age_to: Optional[int] = None
    apps: Optional[str] = None
    apps_not: Optional[str] = None
    birthday: Optional[int] = None
    cities: Optional[str] = None
    cities_not: Optional[str] = None
    country: Optional[int] = None
    districts: Optional[str] = None
    groups: Optional[str] = None
    interest_categories: Optional[str] = None
    interests: Optional[str] = None
    paying: Optional[bool] = None
    positions: Optional[str] = None
    religions: Optional[str] = None
    retargeting_groups: Optional[str] = None
    retargeting_groups_not: Optional[str] = None
    school_from: Optional[int] = None
    school_to: Optional[int] = None
    schools: Optional[str] = None
    sex: Optional[AdsCriteriaSex] = None
    stations: Optional[str] = None
    statuses: Optional[str] = None
    streets: Optional[str] = None
    travellers: Optional[BasePropertyExists] = None
    uni_from: Optional[int] = None
    uni_to: Optional[int] = None
    user_browsers: Optional[str] = None
    user_devices: Optional[str] = None
    user_os: Optional[str] = None
