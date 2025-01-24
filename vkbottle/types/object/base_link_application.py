from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ..base import VkObject

if TYPE_CHECKING:
    from .base_link_application_store import BaseLinkApplicationStore


class BaseLinkApplication(VkObject):
    """VK Object BaseLinkApplication

    app_id - Application Id
    store -
    """

    app_id: Optional[float] = None
    store: Optional[BaseLinkApplicationStore] = None
