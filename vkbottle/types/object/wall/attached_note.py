from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class AttachedNote(VkObject):
    """VK Object WallAttachedNote

    can_comment -
    comments - Comments number
    date - Date when the note has been created in Unixtime
    id - Note ID
    owner_id - Note owner's ID
    privacy_comment -
    privacy_view -
    read_comments - Read comments number
    text - Note text
    text_wiki - Note wiki text
    title - Note title
    view_url - URL of the page with note preview
    """

    can_comment: Optional[int] = None
    comments: int
    date: int
    id: int
    owner_id: int
    privacy_comment: Optional[List[str]] = None
    privacy_view: Optional[List[str]] = None
    read_comments: int
    text: Optional[str] = None
    text_wiki: Optional[str] = None
    title: str
    view_url: str
