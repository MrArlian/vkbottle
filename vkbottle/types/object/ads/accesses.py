from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AdsAccessRole

from ...base import VkObject


class Accesses(VkObject):
    """VK Object AdsAccesses

    client_id - Client ID
    role -
    """

    client_id: Optional[str] = None
    role: Optional[AdsAccessRole] = None
