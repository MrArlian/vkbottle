from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import UtilsLinkCheckedStatus

from ...base import VkObject


class LinkChecked(VkObject):
    """VK Object UtilsLinkChecked

    link - Link URL
    status -
    """

    link: Optional[str] = None
    status: Optional[UtilsLinkCheckedStatus] = None
