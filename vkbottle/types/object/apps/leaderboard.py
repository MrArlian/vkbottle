from __future__ import annotations

from typing import Optional

from ...base import VkObject


class Leaderboard(VkObject):
    """VK Object AppsLeaderboard

    level - Level
    points - Points number
    score - Score number
    user_id - User ID
    """

    level: Optional[int] = None
    points: Optional[int] = None
    score: Optional[int] = None
    user_id: int
