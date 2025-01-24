from __future__ import annotations

from typing import Optional

from ..base import VkObject


class AudioAudio(VkObject):
    """VK Object AudioAudio

    access_key - Access key for the audio
    album_id - Album ID
    artist - Artist name
    date - Date when uploaded
    duration - Duration in seconds
    genre_id - Genre ID
    id - Audio ID
    owner_id - Audio owner's ID
    performer - Performer name
    title - Title
    url - URL of mp3 file
    """

    access_key: Optional[str] = None
    album_id: Optional[int] = None
    artist: str
    date: Optional[int] = None
    duration: int
    genre_id: Optional[int] = None
    id: int
    owner_id: int
    performer: Optional[str] = None
    title: str
    url: Optional[str] = None
