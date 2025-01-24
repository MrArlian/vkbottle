from __future__ import annotations

from ...base import VkObject


class Answer(VkObject):
    """VK Object PollsAnswer

    id - Answer ID
    rate - Answer rate in percents
    text - Answer text
    votes - Votes number
    """

    id: int
    rate: float
    text: str
    votes: int
