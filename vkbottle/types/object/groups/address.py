from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from vkbottle.enum.vk_object import GroupsAddressWorkInfoStatus

from ...base import VkObject

if TYPE_CHECKING:
    from .address_timetable import AddressTimetable


class Address(VkObject):
    """VK Object GroupsAddress

    additional_address - Additional address to the place (6 floor, left door)
    address - String address to the place (Nevsky, 28)
    city_id - City id of address
    country_id - Country id of address
    distance - Distance from the point
    id - Address id
    latitude - Address latitude
    longitude - Address longitude
    metro_station_id - Metro id of address
    phone - Address phone
    place_id -
    time_offset - Time offset int minutes from utc time
    timetable - Week timetable for the address
    title - Title of the place (Zinger, etc)
    work_info_status - Status of information about timetable
    """

    additional_address: Optional[str] = None
    address: Optional[str] = None
    city_id: Optional[int] = None
    country_id: Optional[int] = None
    distance: Optional[int] = None
    id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    metro_station_id: Optional[int] = None
    phone: Optional[str] = None
    place_id: Optional[int] = None
    time_offset: Optional[int] = None
    timetable: Optional[AddressTimetable] = None
    title: Optional[str] = None
    work_info_status: Optional[GroupsAddressWorkInfoStatus] = None
