from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Subscription(VkObject):
    """VK Object OrdersSubscription

    app_id - Subscription's application id
    application_name - Subscription's application name
    cancel_reason - Cancel reason
    create_time - Date of creation in Unixtime
    expire_time - Subscription expiration time in Unixtime
    id - Subscription ID
    item_id - Subscription order item
    next_bill_time - Date of next bill in Unixtime
    pending_cancel - Pending cancel state
    period - Subscription period
    period_start_time - Date of last period start in Unixtime
    photo_url - Item photo image url
    price - Subscription price
    status - Subscription status
    test_mode - Is test subscription
    title - Subscription name
    trial_expire_time - Date of trial expire in Unixtime
    update_time - Date of last change in Unixtime
    """

    app_id: Optional[int] = None
    application_name: Optional[str] = None
    cancel_reason: Optional[str] = None
    create_time: int
    expire_time: Optional[int] = None
    id: int
    item_id: str
    next_bill_time: Optional[int] = None
    pending_cancel: Optional[bool] = None
    period: int
    period_start_time: int
    photo_url: Optional[str] = None
    price: int
    status: str
    test_mode: Optional[bool] = None
    title: Optional[str] = None
    trial_expire_time: Optional[int] = None
    update_time: int
