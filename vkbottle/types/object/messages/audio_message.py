from __future__ import annotations

from typing import List, Optional

from ...base import VkObject


class AudioMessage(VkObject):
    """VK Object MessagesAudioMessage

    access_key - Access key for audio message
    duration - Audio message duration in seconds
    id - Audio message ID
    link_mp3 - MP3 file URL
    link_ogg - OGG file URL
    owner_id - Audio message owner ID
    transcript_error -
    waveform -
    """

    access_key: Optional[str] = None
    duration: int
    id: int
    link_mp3: str
    link_ogg: str
    owner_id: int
    transcript_error: Optional[int] = None
    waveform: List[int]
