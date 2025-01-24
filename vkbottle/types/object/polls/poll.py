from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...base import VkObject

if TYPE_CHECKING:
    from .background import Background
    from .answer import Answer
    from .friend import Friend


class Poll(VkObject):
    """VK Object PollsPoll

    anonymous -
    answer_id - Current user's answer ID
    answer_ids - Current user's answer IDs
    answers -
    author_id - Poll author's ID
    background -
    can_edit -
    can_report -
    can_share -
    can_vote -
    closed -
    created - Date when poll has been created in Unixtime
    disable_unvote -
    embed_hash -
    end_date -
    friends -
    id - Poll ID
    is_board -
    multiple - Information whether the poll with multiple choices
    owner_id - Poll owner's ID
    photo -
    question - Poll question
    votes - Votes number
    """

    anonymous: Optional[bool] = None
    answer_id: Optional[int] = None
    answer_ids: Optional[List[int]] = None
    answers: List[Answer]
    author_id: Optional[int] = None
    background: Optional[Background] = None
    can_edit: bool
    can_report: bool
    can_share: bool
    can_vote: bool
    closed: bool
    created: int
    disable_unvote: bool
    embed_hash: Optional[str] = None
    end_date: int
    friends: Optional[List[Friend]] = None
    id: int
    is_board: bool
    multiple: bool
    owner_id: int
    photo: Optional[Background] = None
    question: str
    votes: int

