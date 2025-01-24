from __future__ import annotations

from typing import Optional

from ...base import VkObject


class University(VkObject):
    """VK Object UsersUniversity

    chair - Chair ID
    chair_name - Chair name
    city - City ID
    country - Country ID
    education_form - Education form
    education_status - Education status
    faculty - Faculty ID
    faculty_name - Faculty name
    graduation - Graduation year
    id - University ID
    name - University name
    university_group_id -
    """

    chair: Optional[int] = None
    chair_name: Optional[str] = None
    city: Optional[int] = None
    country: Optional[int] = None
    education_form: Optional[str] = None
    education_status: Optional[str] = None
    faculty: Optional[int] = None
    faculty_name: Optional[str] = None
    graduation: Optional[int] = None
    id: Optional[int] = None
    name: Optional[str] = None
    university_group_id: Optional[int] = None
