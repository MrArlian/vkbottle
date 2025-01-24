from __future__ import annotations

from typing import Optional

from ...base import VkObject


class LiveSettings(VkObject):
    """VK Object VideoLiveSettings

    can_rewind - If user car rewind live or not
    is_endless - If live is endless or not
    max_duration - Max possible time for rewind
    """

    can_rewind: Optional[bool] = None
    is_endless: Optional[bool] = None
    max_duration: Optional[int] = None
