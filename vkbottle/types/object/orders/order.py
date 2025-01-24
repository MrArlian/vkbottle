from __future__ import annotations

from typing import Optional

from vkbottle.enum.vk_object import OrderStatus

from ...base import VkObject


class Order(VkObject):
    """VK Object OrdersOrder

    amount - Amount
    app_order_id - App order ID
    cancel_transaction_id - Cancel transaction ID
    date - Date of creation in Unixtime
    id - Order ID
    item - Order item
    receiver_id - Receiver ID
    status - Order status
    transaction_id - Transaction ID
    user_id - User ID
    """

    amount: str
    app_order_id: str
    cancel_transaction_id: Optional[str] = None
    date: str
    id: str
    item: str
    receiver_id: str
    status: OrderStatus
    transaction_id: Optional[str] = None
    user_id: str
