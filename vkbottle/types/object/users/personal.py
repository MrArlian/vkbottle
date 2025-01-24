from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class Personal(VkObject):
    """VK Object UsersPersonal

    alcohol - User's views on alcohol
    inspired_by - User's inspired by
    langs -
    life_main - User's personal priority in life
    people_main - User's personal priority in people
    political - User's political views
    religion - User's religion
    religion_id - User's religion id
    smoking - User's views on smoking
    """

    alcohol: Optional[int] = None
    inspired_by: Optional[str] = None
    langs: Optional[List[str]] = None
    life_main: Optional[int] = None
    people_main: Optional[int] = None
    political: Optional[int] = None
    religion: Optional[str] = None
    religion_id: Optional[int] = None
    smoking: Optional[int] = None
