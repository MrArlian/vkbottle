from __future__ import annotations

from typing import Optional

from ...base import VkObject


class School(VkObject):
    """VK Object UsersSchool

    city - City ID
    _class - School class letter
    country - Country ID
    id - School ID
    name - School name
    speciality -
    type - School type ID
    type_str - School type name
    year_from - Year the user started to study
    year_graduated - Graduation year
    year_to - Year the user finished to study
    """

    city: Optional[int] = None
    _class: Optional[str] = None
    country: Optional[int] = None
    id: Optional[str] = None
    name: Optional[str] = None
    speciality: Optional[str] = None
    type: Optional[int] = None
    type_str: Optional[str] = None
    year_from: Optional[int] = None
    year_graduated: Optional[int] = None
    year_to: Optional[int] = None
