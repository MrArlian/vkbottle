from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .long_poll_events import LongPollEvents


class LongPollSettings(VkObject):
    """VK Object GroupsLongPollSettings

    api_version - API version used for the events
    events -
    is_enabled - Shows whether Long Poll is enabled
    """

    api_version: Optional[str] = None
    events: LongPollEvents
    is_enabled: bool
