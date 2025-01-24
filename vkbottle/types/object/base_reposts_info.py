from __future__ import annotations

from typing import Optional

from ..base import VkObject


class BaseRepostsInfo(VkObject):
    """VK Object BaseRepostsInfo

    count - Total reposts counter. Sum of wall and mail reposts counters
    mail_count - Mail reposts counter
    user_reposted - Information whether current user has reposted the post
    wall_count - Wall reposts counter
    """

    count: int
    mail_count: Optional[int] = None
    user_reposted: Optional[int] = None
    wall_count: Optional[int] = None
