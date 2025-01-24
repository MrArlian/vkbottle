from __future__ import annotations

from typing import Optional

from ...base import VkObject


class ContactsItem(VkObject):
    """VK Object GroupsContactsItem

    desc - Contact description
    email - Contact email
    phone - Contact phone
    user_id - User ID
    """

    desc: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    user_id: Optional[int] = None
