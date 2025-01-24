from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Transaction(VkObject):
    """VK Object SecureTransaction

    date - Transaction date in Unixtime
    id - Transaction ID
    uid_from - From ID
    uid_to - To ID
    votes - Votes number
    """

    date: Optional[int] = None
    id: Optional[int] = None
    uid_from: Optional[int] = None
    uid_to: Optional[int] = None
    votes: Optional[int] = None
