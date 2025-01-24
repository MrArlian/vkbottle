from __future__ import annotations

from vkbottle.enum.vk_object import DonutDonatorSubscriptionInfoStatus

from ...base import VkObject


class DonatorSubscriptionInfo(VkObject):
    """VK Object DonutDonatorSubscriptionInfo"""

    amount: int
    next_payment_date: int
    owner_id: int
    status: DonutDonatorSubscriptionInfoStatus
