from __future__ import annotations

from typing import Optional

from ...base import VkObject


class PushSettings(VkObject):
    """VK Object MessagesPushSettings

    disabled_forever - Information whether push notifications are disabled forever
    disabled_mass_mentions - Information whether the mass mentions (like '@all', '@online') are disabled
    disabled_mentions - Information whether the mentions are disabled
    disabled_until - Time until what notifications are disabled
    no_sound - Information whether the sound is on
    """

    disabled_forever: bool
    disabled_mass_mentions: Optional[bool] = None
    disabled_mentions: Optional[bool] = None
    disabled_until: Optional[int] = None
    no_sound: bool
