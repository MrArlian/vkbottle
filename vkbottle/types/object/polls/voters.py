from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .voters_users import VotersUsers


class Voters(VkObject):
    """VK Object PollsVoters

    answer_id - Answer ID
    users -
    """

    answer_id: Optional[int] = None
    users: Optional[VotersUsers] = None
