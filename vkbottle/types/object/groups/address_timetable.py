from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .address_timetable_day import AddressTimetableDay


class AddressTimetable(VkObject):
    """VK Object GroupsAddressTimetable

    fri - Timetable for friday
    mon - Timetable for monday
    sat - Timetable for saturday
    sun - Timetable for sunday
    thu - Timetable for thursday
    tue - Timetable for tuesday
    wed - Timetable for wednesday
    """

    fri: Optional[AddressTimetableDay] = None
    mon: Optional[AddressTimetableDay] = None
    sat: Optional[AddressTimetableDay] = None
    sun: Optional[AddressTimetableDay] = None
    thu: Optional[AddressTimetableDay] = None
    tue: Optional[AddressTimetableDay] = None
    wed: Optional[AddressTimetableDay] = None
