from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AdsTargSuggestionsSchoolsType

from ...base import VkObject


class TargSuggestionsSchools(VkObject):
    """VK Object AdsTargSuggestionsSchools

    desc - Full school title
    id - School ID
    name - School title
    parent - City name
    type -
    """

    desc: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    parent: Optional[str] = None
    type: Optional[AdsTargSuggestionsSchoolsType] = None
