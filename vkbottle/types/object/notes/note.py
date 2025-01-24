from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class Note(VkObject):
    """VK Object NotesNote

    can_comment - Information whether current user can comment the note
    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    privacy_comment -
    privacy_view -
    read_comments -
    text - Note text
    text_wiki - Note text in wiki format
    title - Note title
    view_url - URL of the page with note preview
    """

    can_comment: Optional[bool] = None
    comments: int
    date: int
    id: int
    owner_id: int
    privacy_comment: Optional[List[str]] = None
    privacy_view: Optional[List[str]] = None
    read_comments: Optional[int] = None
    text: Optional[str] = None
    text_wiki: Optional[str] = None
    title: str
    view_url: str
