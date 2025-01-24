from __future__ import annotations

from vkbottle.enum.vk_object import AdsAccountType, AdsAccessRole

from ...base import VkObject


class Account(VkObject):
    """VK Object AdsAccount

    access_role -
    account_id - Account ID
    account_name - Account name
    account_status - Information whether account is active
    account_type -
    can_view_budget - Can user view account budget
    """

    access_role: AdsAccessRole
    account_id: int
    account_name: str
    account_status: bool
    account_type: AdsAccountType
    can_view_budget: bool
