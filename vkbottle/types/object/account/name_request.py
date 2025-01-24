from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import AccountNameRequestStatus

from ...base import VkObject


class NameRequest(VkObject):
    """VK Object AccountNameRequest

    first_name - First name in request
    id - Request ID needed to cancel the request
    lang - Text to display to user
    last_name - Last name in request
    link_href - href for link in lang field
    link_label - label to display for link in lang field
    status -
    """

    first_name: Optional[str] = None
    id: Optional[int] = None
    lang: Optional[str] = None
    last_name: Optional[str] = None
    link_href: Optional[str] = None
    link_label: Optional[str] = None
    status: Optional[AccountNameRequestStatus] = None
