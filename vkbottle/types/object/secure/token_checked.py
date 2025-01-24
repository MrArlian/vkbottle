from __future__ import annotations

from typing import Optional

from ...base import VkObject


class TokenChecked(VkObject):
    """VK Object SecureTokenChecked

    date - Date when access_token has been generated in Unixtime
    expire - Date when access_token will expire in Unixtime
    success - Returns if successfully processed
    user_id - User ID
    """

    date: Optional[int] = None
    expire: Optional[int] = None
    success: Optional[int] = None
    user_id: Optional[int] = None
