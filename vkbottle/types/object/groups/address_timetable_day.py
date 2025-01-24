from __future__ import annotations

from typing import Optional

from ...base import VkObject


class AddressTimetableDay(VkObject):
    """VK Object GroupsAddressTimetableDay

    break_close_time - Close time of the break in minutes
    break_open_time - Start time of the break in minutes
    close_time - Close time in minutes
    open_time - Open time in minutes
    """

    break_close_time: Optional[int] = None
    break_open_time: Optional[int] = None
    close_time: int
    open_time: int
