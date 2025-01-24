from __future__ import annotations

from typing import Optional

from ..users.user_xtr_type import UserXtrType


class UserXtrInvitedBy(UserXtrType):
    """VK Object MessagesUserXtrInvitedBy

    invited_by - ID of the inviter
    """

    invited_by: Optional[int] = None
