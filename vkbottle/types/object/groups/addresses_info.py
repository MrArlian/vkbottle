from __future__ import annotations

from typing import Optional

from ...base import VkObject


class AddressesInfo(VkObject):
    """VK Object GroupsAddressesInfo

    is_enabled - Information whether addresses is enabled
    main_address_id - Main address id for group
    """

    is_enabled: bool
    main_address_id: Optional[int] = None
