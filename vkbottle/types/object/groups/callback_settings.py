from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .long_poll_events import LongPollEvents


class CallbackSettings(VkObject):
    """VK Object GroupsCallbackSettings

    api_version - API version used for the events
    events -
    """

    api_version: Optional[str] = None
    events: Optional[LongPollEvents] = None
