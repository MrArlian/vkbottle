from typing import Optional

from ..base import VkObject

from .group_settings_changes import GroupSettingsChanges


class GroupChangeSettings(VkObject):
    changes: Optional[GroupSettingsChanges] = None
    user_id: int
