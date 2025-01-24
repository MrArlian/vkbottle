from __future__ import annotations

from typing import Optional

from ...base import VkObject


class NoteComment(VkObject):
    """VK Object NotesNoteComment

    date - Date when the comment has beed added in Unixtime
    id - Comment ID
    message - Comment text
    nid - Note ID
    oid - Note ID
    reply_to - ID of replied comment
    uid - Comment author's ID
    """

    date: int
    id: int
    message: str
    nid: int
    oid: int
    reply_to: Optional[int] = None
    uid: int
